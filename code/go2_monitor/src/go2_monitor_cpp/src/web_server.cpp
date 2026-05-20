#include "go2_monitor_cpp/web_server.hpp"
#include "go2_monitor_cpp/viewer_data_source.hpp"

#include <arpa/inet.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <poll.h>
#include <sys/socket.h>
#include <unistd.h>

#include <array>
#include <cctype>
#include <cerrno>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

namespace {

constexpr const char* RosaNavHost = "192.168.0.90";
constexpr int kRemoteInstructionPort = 5000;
constexpr const char* kRemoteInstructionPath = "/query";
constexpr const char* kFallbackViewerImageName = "example.png";
constexpr int kConnectTimeoutMs = 2000;
constexpr int kRequestIoTimeoutMs = 100000;

struct InstructionRequestResult {
  bool ok = false;
  int status_code = 0;
  std::string body;
  std::string error;
};

bool decode_base64(std::string_view input, std::string& output) {
  static const std::array<int, 256> table = []() {
    std::array<int, 256> values {};
    values.fill(-1);
    for (int i = 0; i < 26; ++i) {
      values[static_cast<unsigned char>('A' + i)] = i;
      values[static_cast<unsigned char>('a' + i)] = 26 + i;
    }
    for (int i = 0; i < 10; ++i) {
      values[static_cast<unsigned char>('0' + i)] = 52 + i;
    }
    values[static_cast<unsigned char>('+')] = 62;
    values[static_cast<unsigned char>('/')] = 63;
    return values;
  }();

  output.clear();
  int value = 0;
  int bits = -8;
  for (const unsigned char ch : input) {
    if (std::isspace(ch)) {
      continue;
    }
    if (ch == '=') {
      break;
    }

    const int decoded = table[ch];
    if (decoded < 0) {
      return false;
    }

    value = (value << 6) | decoded;
    bits += 6;
    if (bits >= 0) {
      output.push_back(static_cast<char>((value >> bits) & 0xFF));
      bits -= 8;
    }
  }

  return true;
}

bool extract_json_string_field(
  const std::string& payload,
  const char* field_name,
  std::string& value) {
  const std::regex pattern(
    std::string("\"") + field_name + "\"\\s*:\\s*\"([^\"]*)\"");
  std::smatch match;
  if (!std::regex_search(payload, match, pattern) || match.size() < 2) {
    return false;
  }

  value = match[1].str();
  return true;
}

bool parse_pointing_preview(
  const std::string& payload,
  std::string& mime_type,
  std::string& image_bytes) {
  std::string base64_bytes;
  if (!extract_json_string_field(payload, "mime_type", mime_type) ||
      !extract_json_string_field(payload, "base64", base64_bytes)) {
    return false;
  }

  if (!decode_base64(base64_bytes, image_bytes) || image_bytes.empty()) {
    return false;
  }

  return true;
}

struct SocketHandle {
  int fd = -1;

  ~SocketHandle() {
    if (fd >= 0) {
      ::close(fd);
    }
  }
};

bool write_all(int fd, const std::string& data, std::string& error) {
  std::size_t written = 0;
  while (written < data.size()) {
    const ssize_t rc = ::send(fd, data.data() + written, data.size() - written, 0);
    if (rc < 0) {
      if (errno == EINTR) {
        continue;
      }
      error = "failed to write instruction request: " + std::string(std::strerror(errno));
      return false;
    }
    if (rc == 0) {
      error = "failed to write instruction request: connection closed";
      return false;
    }
    written += static_cast<std::size_t>(rc);
  }
  return true;
}

bool connect_with_timeout(int fd, const sockaddr_in& address, std::string& error) {
  const int flags = ::fcntl(fd, F_GETFL, 0);
  if (flags < 0) {
    error = "failed to inspect request socket flags: " + std::string(std::strerror(errno));
    return false;
  }

  if (::fcntl(fd, F_SETFL, flags | O_NONBLOCK) < 0) {
    error = "failed to configure request socket: " + std::string(std::strerror(errno));
    return false;
  }

  int rc = ::connect(fd, reinterpret_cast<const sockaddr*>(&address), sizeof(address));
  if (rc < 0 && errno == EINPROGRESS) {
    pollfd descriptor {};
    descriptor.fd = fd;
    descriptor.events = POLLOUT;

    while (true) {
      rc = ::poll(&descriptor, 1, kConnectTimeoutMs);
      if (rc < 0 && errno == EINTR) {
        continue;
      }
      break;
    }

    if (rc == 0) {
      error = "failed to connect to request endpoint: timed out";
      return false;
    }
    if (rc < 0) {
      error = "failed to wait for request endpoint: " + std::string(std::strerror(errno));
      return false;
    }

    int socket_error = 0;
    socklen_t socket_error_size = sizeof(socket_error);
    if (::getsockopt(fd, SOL_SOCKET, SO_ERROR, &socket_error, &socket_error_size) < 0) {
      error = "failed to inspect request socket: " + std::string(std::strerror(errno));
      return false;
    }
    if (socket_error != 0) {
      error = "failed to connect to request endpoint: " + std::string(std::strerror(socket_error));
      return false;
    }
  } else if (rc < 0) {
    error = "failed to connect to request endpoint: " + std::string(std::strerror(errno));
    return false;
  }

  if (::fcntl(fd, F_SETFL, flags) < 0) {
    error = "failed to restore request socket flags: " + std::string(std::strerror(errno));
    return false;
  }

  timeval timeout {};
  timeout.tv_sec = kRequestIoTimeoutMs / 1000;
  timeout.tv_usec = (kRequestIoTimeoutMs % 1000) * 1000;
  if (::setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0 ||
      ::setsockopt(fd, SOL_SOCKET, SO_SNDTIMEO, &timeout, sizeof(timeout)) < 0) {
    error = "failed to configure request socket timeout: " + std::string(std::strerror(errno));
    return false;
  }

  return true;
}

InstructionRequestResult post_request(
  const char* host,
  int port,
  const char* path,
  const char* content_type,
  const std::string& body) {
  InstructionRequestResult result;

  SocketHandle socket_handle;
  socket_handle.fd = ::socket(AF_INET, SOCK_STREAM, 0);
  if (socket_handle.fd < 0) {
    result.error = "failed to open request socket: " + std::string(std::strerror(errno));
    return result;
  }

  sockaddr_in address {};
  address.sin_family = AF_INET;
  address.sin_port = htons(static_cast<std::uint16_t>(port));
  if (::inet_pton(AF_INET, host, &address.sin_addr) != 1) {
    result.error = "failed to parse request endpoint address";
    return result;
  }

  if (!connect_with_timeout(socket_handle.fd, address, result.error)) {
    return result;
  }

  std::ostringstream request_stream;
  request_stream
    << "POST " << path << " HTTP/1.1\r\n"
    << "Host: " << host << ":" << port << "\r\n"
    << "Content-Type: " << content_type << "\r\n"
    << "Content-Length: " << body.size() << "\r\n"
    << "Connection: close\r\n"
    << "\r\n"
    << body;
  const std::string request = request_stream.str();

  if (!write_all(socket_handle.fd, request, result.error)) {
    return result;
  }

  ::shutdown(socket_handle.fd, SHUT_WR);

  std::array<char, 4096> buffer {};
  std::string raw_response;
  while (true) {
    const ssize_t rc = ::recv(socket_handle.fd, buffer.data(), buffer.size(), 0);
    if (rc < 0) {
      if (errno == EINTR) {
        continue;
      }
      result.error = "failed to read request response: " + std::string(std::strerror(errno));
      return result;
    }
    if (rc == 0) {
      break;
    }
    raw_response.append(buffer.data(), static_cast<std::size_t>(rc));
  }

  const std::size_t status_line_end = raw_response.find("\r\n");
  const std::size_t header_end = raw_response.find("\r\n\r\n");
  if (status_line_end == std::string::npos || header_end == std::string::npos) {
    result.error = "request endpoint returned an invalid HTTP response";
    return result;
  }

  std::istringstream status_stream(raw_response.substr(0, status_line_end));
  std::string http_version;
  status_stream >> http_version >> result.status_code;
  if (!status_stream || http_version.rfind("HTTP/", 0) != 0) {
    result.error = "request endpoint returned an invalid HTTP status line";
    return result;
  }

  result.body = raw_response.substr(header_end + 4);
  result.ok = result.status_code >= 200 && result.status_code < 300;
  if (!result.ok) {
    if (!result.body.empty()) {
      result.error = result.body;
    } else {
      result.error = "request endpoint returned HTTP " + std::to_string(result.status_code);
    }
  }

  return result;
}

InstructionRequestResult forward_instruction_request(const std::string& instruction) {
  return post_request(
    RosaNavHost,
    kRemoteInstructionPort,
    kRemoteInstructionPath,
    "text/plain; charset=utf-8",
    instruction);
}

InstructionRequestResult forward_pointing_request(const std::string& payload) {
  return post_request(
    RosaNavHost,
    kRemoteInstructionPort,
    kRemoteInstructionPath,
    "application/json; charset=utf-8",
    payload);
}

crow::json::wvalue make_unavailable_response(const char* error) {
  crow::json::wvalue response;
  response["ok"] = false;
  response["error"] = error;
  return response;
}

crow::json::wvalue make_source_error_response(const go2_monitor_cpp::ViewerDataSource& viewer_data_source) {
  crow::json::wvalue response;
  response["ok"] = false;
  response["source"] = viewer_data_source.source_label();
  response["source_mode"] = viewer_data_source.source_mode();
  response["error"] = viewer_data_source.last_error();
  return response;
}

crow::json::wvalue::list build_topic_list(const std::vector<go2_monitor_cpp::TopicInfo>& topics) {
  crow::json::wvalue::list topic_list;
  topic_list.reserve(topics.size());

  for (const auto& topic : topics) {
    crow::json::wvalue item;
    item["name"] = topic.name;
    item["type"] = topic.type;
    topic_list.emplace_back(std::move(item));
  }

  return topic_list;
}

std::string make_viewer_image_url(
  std::size_t index,
  const char* stream,
  const go2_monitor_cpp::ViewerFrameInfo& frame,
  const std::string& source_mode) {
  const bool is_rgb = std::strcmp(stream, "rgb") == 0;
  std::string url = "/api/viewer/image?stream=";
  url += stream;
  url += "&index=";
  url += std::to_string(index);
  if (source_mode == "zenoh") {
    const auto revision = is_rgb ? frame.rgb_revision : frame.depth_revision;
    url += "&rev=" + std::to_string(revision);
  }
  return url;
}

crow::json::wvalue::list build_frame_list(const go2_monitor_cpp::ViewerSnapshot& snapshot) {
  crow::json::wvalue::list frame_list;
  frame_list.reserve(snapshot.frames.size());

  for (const auto& frame : snapshot.frames) {
    crow::json::wvalue item;
    item["index"] = static_cast<long long>(frame.index);
    item["rgb_url"] = make_viewer_image_url(frame.index, "rgb", frame, snapshot.source_mode);
    if (!snapshot.depth_topic.empty()) {
      item["depth_url"] = make_viewer_image_url(frame.index, "depth", frame, snapshot.source_mode);
    }
    frame_list.emplace_back(std::move(item));
  }

  return frame_list;
}

crow::json::wvalue::list build_timeline_list(
  const std::vector<go2_monitor_cpp::PlaybackTimelineEntry>& timeline) {
  crow::json::wvalue::list timeline_list;
  timeline_list.reserve(timeline.size());

  for (const auto& entry : timeline) {
    crow::json::wvalue item;
    item["index"] = static_cast<long long>(entry.index);
    item["viewer_frame_index"] = static_cast<long long>(entry.viewer_frame_index);
    item["timestamp"] = entry.timestamp;
    item["has_odom"] = entry.has_odom;
    item["odom_index"] = static_cast<long long>(entry.odom_index);
    item["odom_timestamp"] = entry.odom_timestamp;
    item["odom_x"] = entry.odom_x;
    item["odom_y"] = entry.odom_y;
    item["has_stdout"] = entry.has_stdout;
    item["stdout_index"] = static_cast<long long>(entry.stdout_index);
    timeline_list.emplace_back(std::move(item));
  }

  return timeline_list;
}

crow::json::wvalue::list build_trajectory_list(
  const std::vector<go2_monitor_cpp::TrajectoryPoint>& trajectory) {
  crow::json::wvalue::list trajectory_list;
  trajectory_list.reserve(trajectory.size());

  for (const auto& point : trajectory) {
    crow::json::wvalue item;
    item["timestamp"] = point.timestamp;
    item["x"] = point.x;
    item["y"] = point.y;
    item["has_yaw"] = point.has_yaw;
    item["yaw"] = point.yaw;
    trajectory_list.emplace_back(std::move(item));
  }

  return trajectory_list;
}

crow::json::wvalue::list build_stdout_list(
  const std::vector<go2_monitor_cpp::StdoutEntry>& stdout_entries) {
  crow::json::wvalue::list stdout_list;
  stdout_list.reserve(stdout_entries.size());

  for (const auto& entry : stdout_entries) {
    crow::json::wvalue item;
    item["timestamp"] = entry.timestamp;
    item["message"] = entry.message;
    stdout_list.emplace_back(std::move(item));
  }

  return stdout_list;
}

crow::json::wvalue make_topics_response(
  const go2_monitor_cpp::ViewerDataSource& viewer_data_source,
  const std::vector<go2_monitor_cpp::TopicInfo>& topics) {
  crow::json::wvalue response;
  response["ok"] = true;
  response["source"] = viewer_data_source.source_label();
  response["source_mode"] = viewer_data_source.source_mode();
  response["topics"] = build_topic_list(topics);
  return response;
}

crow::json::wvalue make_viewer_snapshot_response(const go2_monitor_cpp::ViewerSnapshot& snapshot) {
  crow::json::wvalue response;
  response["ok"] = true;
  response["source"] = snapshot.source;
  response["source_mode"] = snapshot.source_mode;
  response["supports_playback"] = snapshot.supports_playback;
  response["revision"] = static_cast<unsigned long long>(snapshot.revision);
  response["rgb_revision"] = static_cast<unsigned long long>(snapshot.rgb_revision);
  response["depth_revision"] = static_cast<unsigned long long>(snapshot.depth_revision);
  response["pointing_preview_active"] = snapshot.pointing_preview_active;
  response["awaiting_live_rgb_after_pointing"] = snapshot.awaiting_live_rgb_after_pointing;
  response["rgb_stale_after_pointing"] = snapshot.rgb_stale_after_pointing;
  response["rgb_topic"] = snapshot.rgb_topic;
  response["depth_topic"] = snapshot.depth_topic;
  response["stdout_topic"] = snapshot.stdout_topic;
  response["total_frames"] = static_cast<long long>(snapshot.frames.size());
  response["total_timeline_entries"] = static_cast<long long>(snapshot.timeline.size());
  response["frames"] = build_frame_list(snapshot);
  response["timeline"] = build_timeline_list(snapshot.timeline);
  response["trajectory"] = build_trajectory_list(snapshot.trajectory);
  response["stdout_entries"] = build_stdout_list(snapshot.stdout_entries);
  return response;
}

crow::response make_viewer_image_response(
  go2_monitor_cpp::ViewerDataSource& viewer_data_source,
  const crow::request& req) {
  const char* stream = req.url_params.get("stream");
  const char* index_param = req.url_params.get("index");
  if (stream == nullptr || index_param == nullptr) {
    return crow::response(400, "missing stream or index");
  }

  std::size_t index = 0;
  try {
    index = static_cast<std::size_t>(std::stoull(index_param));
  } catch (...) {
    return crow::response(400, "invalid index");
  }

  std::string mime_type;
  std::string image_bytes;
  if (!viewer_data_source.render_viewer_image(index, stream, mime_type, image_bytes)) {
    return crow::response(404, viewer_data_source.last_error());
  }

  crow::response response;
  response.code = 200;
  response.set_header("Content-Type", mime_type);
  response.set_header("Cache-Control", "no-store");
  response.body = std::move(image_bytes);
  return response;
}

crow::json::wvalue make_instruction_response(const InstructionRequestResult& result) {
  crow::json::wvalue response;
  response["ok"] = result.ok;
  response["status_code"] = result.status_code;
  response["response"] = result.body;
  if (!result.ok) {
    response["error"] = result.error;
  }
  return response;
}

std::filesystem::path find_fallback_viewer_image_path() {
  namespace fs = std::filesystem;

  const std::array<fs::path, 3> candidate_paths = {
    fs::current_path() / kFallbackViewerImageName,
    fs::current_path().parent_path() / kFallbackViewerImageName,
    fs::path(__FILE__).parent_path().parent_path().parent_path().parent_path() / kFallbackViewerImageName,
  };

  for (const auto& path : candidate_paths) {
    if (fs::exists(path) && fs::is_regular_file(path)) {
      return path;
    }
  }

  return {};
}

crow::response make_fallback_viewer_image_response() {
  const auto path = find_fallback_viewer_image_path();
  if (path.empty()) {
    return crow::response(404, "fallback viewer image was not found");
  }

  std::ifstream input(path, std::ios::in | std::ios::binary);
  if (!input) {
    return crow::response(500, "failed to open fallback viewer image");
  }

  std::ostringstream buffer;
  buffer << input.rdbuf();
  if (!input.good() && !input.eof()) {
    return crow::response(500, "failed to read fallback viewer image");
  }

  crow::response response;
  response.code = 200;
  response.set_header("Content-Type", "image/png");
  response.set_header("Cache-Control", "no-store");
  response.body = buffer.str();
  return response;
}

}  // namespace

namespace go2_monitor_cpp {

void WebSocketHub::add(crow::websocket::connection* conn) {
  std::lock_guard<std::mutex> lock(mutex_);
  conns_.insert(conn);
}

void WebSocketHub::remove(crow::websocket::connection* conn) {
  std::lock_guard<std::mutex> lock(mutex_);
  conns_.erase(conn);
}

void WebSocketHub::broadcast(const std::string& msg) {
  std::lock_guard<std::mutex> lock(mutex_);
  for (auto* conn : conns_) {
    if (conn != nullptr) {
      conn->send_text(msg);
    }
  }
}

WebServer::WebServer(
  std::shared_ptr<WebSocketHub> ws_hub,
  std::shared_ptr<ViewerDataSource> viewer_data_source,
  std::string initial_ws_message)
: ws_hub_(std::move(ws_hub)),
  viewer_data_source_(std::move(viewer_data_source)),
  initial_ws_message_(std::move(initial_ws_message)) {
  setup_routes();
}

void WebServer::run(uint16_t port) {
  app_.loglevel(crow::LogLevel::Warning);
  std::cout << "go2_monitor listening on http://127.0.0.1:" << port << std::endl;
  app_.port(port).multithreaded().run();
}

void WebServer::stop() {
  app_.stop();
}

void WebServer::setup_routes() {
  CROW_ROUTE(app_, "/")([this]() {
    return index_html();
  });

  CROW_ROUTE(app_, "/api/topics")([this]() {
    if (!viewer_data_source_) {
      return make_unavailable_response(
        "topic api is available only when the current source exposes viewer data");
    }

    std::vector<TopicInfo> topics;
    if (!viewer_data_source_->list_topics(topics)) {
      return make_source_error_response(*viewer_data_source_);
    }

    return make_topics_response(*viewer_data_source_, topics);
  });

  CROW_ROUTE(app_, "/api/viewer/frames")([this]() {
    if (!viewer_data_source_) {
      return make_unavailable_response(
        "viewer api is available only when the current source exposes viewer data");
    }

    ViewerSnapshot snapshot;
    if (!viewer_data_source_->get_viewer_snapshot(snapshot)) {
      return make_source_error_response(*viewer_data_source_);
    }

    return make_viewer_snapshot_response(snapshot);
  });

  CROW_ROUTE(app_, "/api/viewer/image")([this](const crow::request& req) {
    if (!viewer_data_source_) {
      return crow::response(404, "viewer api is available only when the current source exposes viewer data");
    }

    return make_viewer_image_response(*viewer_data_source_, req);
  });

  CROW_ROUTE(app_, "/api/viewer/fallback-image")([]() {
    return make_fallback_viewer_image_response();
  });

  CROW_ROUTE(app_, "/api/live/instruction")
    .methods(crow::HTTPMethod::POST)([this](const crow::request& req) {
      if (!viewer_data_source_ || viewer_data_source_->source_mode() != "zenoh") {
        return make_unavailable_response("instruction api is available only in zenoh mode");
      }

      if (req.body.empty()) {
        return make_unavailable_response("instruction text is empty");
      }

      return make_instruction_response(forward_instruction_request(req.body));
    });

  CROW_ROUTE(app_, "/api/live/pointing")
    .methods(crow::HTTPMethod::POST)([this](const crow::request& req) {
      if (!viewer_data_source_ || viewer_data_source_->source_mode() != "zenoh") {
        return make_unavailable_response("pointing api is available only in zenoh mode");
      }

      if (req.body.empty()) {
        return make_unavailable_response("pointing payload is empty");
      }

      std::string preview_mime_type;
      std::string preview_image_bytes;
      if (parse_pointing_preview(req.body, preview_mime_type, preview_image_bytes)) {
        viewer_data_source_->accept_pointing_preview(preview_mime_type, preview_image_bytes);
      }

      return make_instruction_response(forward_pointing_request(req.body));
    });

  CROW_WEBSOCKET_ROUTE(app_, "/ws")
    .onopen([this](crow::websocket::connection& conn) {
      ws_hub_->add(&conn);
      if (!initial_ws_message_.empty()) {
        conn.send_text(initial_ws_message_);
      }
    })
    .onclose([this](crow::websocket::connection& conn, const std::string&) {
      ws_hub_->remove(&conn);
    });
}

std::string WebServer::index_html() const {
  namespace fs = std::filesystem;

  const std::array<fs::path, 4> candidate_paths = {
    fs::current_path() / "html" / "ui_preview_dashboard7.html",
    fs::current_path().parent_path() / "html" / "ui_preview_dashboard7.html",
    fs::path(__FILE__).parent_path().parent_path().parent_path().parent_path() / "html" / "ui_preview_dashboard7.html",
    fs::path("/home/alice/go2_monitor/html/ui_preview_dashboard7.html"),
  };

  for (const auto& path : candidate_paths) {
    std::ifstream input(path, std::ios::in | std::ios::binary);
    if (!input) {
      continue;
    }

    std::ostringstream buffer;
    buffer << input.rdbuf();
    if (input.good() || input.eof()) {
      return buffer.str();
    }
  }

  return R"HTML(
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>go2 monitor</title>
</head>
<body style="font-family: sans-serif; padding: 24px;">
  <h1>go2 monitor</h1>
  <p>Failed to load <code>html/ui_preview_dashboard7.html</code>.</p>
</body>
</html>
)HTML";
}

}  // namespace go2_monitor_cpp
