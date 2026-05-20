#include "go2_monitor_cpp/zenoh_monitor.hpp"

#include "go2_monitor_cpp/message_utils.hpp"
#include "go2_monitor_cpp/web_server.hpp"

#include <builtin_interfaces/msg/time.hpp>
#include <nav_msgs/msg/odometry.hpp>
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/compressed_image.hpp>
#include <std_msgs/msg/string.hpp>

#include <array>
#include <chrono>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <string>
#include <string_view>
#include <thread>
#include <vector>

#include <zenoh.hxx>

namespace {

constexpr const char* kRgbTopic = "/camera/color/image_raw/compressed";
constexpr const char* kOdometryTopic = "/utlidar/robot_odom";
constexpr const char* kStdoutTopic = "print";
constexpr auto kEndpointRetryDelay = std::chrono::seconds(1);
constexpr auto kLoopSleep = std::chrono::milliseconds(100);
constexpr auto kRedeclareInterval = std::chrono::milliseconds(250);
constexpr auto kPointingRgbTimeout = std::chrono::milliseconds(1500);

enum class LiveTopic {
  kUnknown,
  kRgb,
  kOdometry,
  kStdout,
};

char normalize_keyexpr_char(char ch) {
  return ch == '%' ? '/' : ch;
}

std::string_view strip_leading_slashes(std::string_view value) {
  while (!value.empty() && normalize_keyexpr_char(value.front()) == '/') {
    value.remove_prefix(1);
  }
  return value;
}

bool keyexpr_matches_topic(std::string_view keyexpr, std::string_view topic) {
  keyexpr = strip_leading_slashes(keyexpr);
  topic = strip_leading_slashes(topic);
  if (keyexpr.size() < topic.size()) {
    return false;
  }

  std::size_t key_index = keyexpr.size();
  for (std::size_t topic_index = topic.size(); topic_index > 0; --topic_index) {
    if (normalize_keyexpr_char(keyexpr[--key_index]) != topic[topic_index - 1]) {
      return false;
    }
  }

  return true;
}

LiveTopic classify_topic(std::string_view keyexpr) {
  if (keyexpr_matches_topic(keyexpr, kRgbTopic)) {
    return LiveTopic::kRgb;
  }
  if (keyexpr_matches_topic(keyexpr, kOdometryTopic)) {
    return LiveTopic::kOdometry;
  }
  if (keyexpr_matches_topic(keyexpr, kStdoutTopic)) {
    return LiveTopic::kStdout;
  }
  return LiveTopic::kUnknown;
}

std::string endpoint_protocol(const std::string& endpoint) {
  const auto separator = endpoint.find('/');
  if (separator == std::string::npos || separator == 0) {
    return "udp";
  }
  return endpoint.substr(0, separator);
}

zenoh::Config make_session_config(const std::string& endpoint) {
  const std::string protocol = endpoint_protocol(endpoint);
  const std::string listen_endpoint = protocol + "/0.0.0.0:0";
  zenoh::Config config = zenoh::Config::create_default();
  config.insert_json5("mode", R"("peer")");
  config.insert_json5("connect/endpoints", std::string("[\"") + endpoint + "\"]");
  config.insert_json5("connect/timeout_ms", "-1");
  config.insert_json5("connect/exit_on_failure", "false");
  config.insert_json5("connect/retry", "{period_init_ms:200, period_max_ms:200, period_increase_factor:1}");
  config.insert_json5("listen/endpoints", std::string("[\"") + listen_endpoint + "\"]");
  config.insert_json5("scouting/multicast/enabled", "false");
  config.insert_json5("scouting/gossip/enabled", "false");
  config.insert_json5("transport/link/protocols", std::string("[\"") + protocol + "\"]");
  return config;
}

std::string make_receive_timestamp() {
  const auto now = std::chrono::system_clock::now();
  const auto seconds = std::chrono::time_point_cast<std::chrono::seconds>(now);
  const auto micros = std::chrono::duration_cast<std::chrono::microseconds>(now - seconds).count();
  const std::time_t tt = std::chrono::system_clock::to_time_t(now);

  std::tm tm {};
  localtime_r(&tt, &tm);

  std::array<char, 32> time_buffer {};
  if (std::strftime(time_buffer.data(), time_buffer.size(), "%Y-%m-%dT%H:%M:%S", &tm) == 0) {
    return {};
  }

  std::array<char, 40> timestamp_buffer {};
  const int written = std::snprintf(
    timestamp_buffer.data(),
    timestamp_buffer.size(),
    "%s.%06lld",
    time_buffer.data(),
    static_cast<long long>(micros));
  if (written <= 0) {
    return {};
  }

  return std::string(timestamp_buffer.data(), static_cast<std::size_t>(written));
}

std::string make_header_timestamp(
  const builtin_interfaces::msg::Time& stamp,
  const std::string& fallback) {
  if (stamp.sec == 0 && stamp.nanosec == 0) {
    return fallback;
  }

  const std::time_t seconds = static_cast<std::time_t>(stamp.sec);
  std::tm tm {};
  localtime_r(&seconds, &tm);

  std::array<char, 32> time_buffer {};
  if (std::strftime(time_buffer.data(), time_buffer.size(), "%Y-%m-%dT%H:%M:%S", &tm) == 0) {
    return fallback;
  }

  std::array<char, 48> timestamp_buffer {};
  const int written = std::snprintf(
    timestamp_buffer.data(),
    timestamp_buffer.size(),
    "%s.%09u",
    time_buffer.data(),
    stamp.nanosec);
  if (written <= 0 || static_cast<std::size_t>(written) >= timestamp_buffer.size()) {
    return fallback;
  }

  return std::string(timestamp_buffer.data(), static_cast<std::size_t>(written));
}

const std::vector<go2_monitor_cpp::TopicInfo>& live_topics() {
  static const std::vector<go2_monitor_cpp::TopicInfo> topics = {
    {kRgbTopic, "sensor_msgs/msg/CompressedImage"},
    {kOdometryTopic, "nav_msgs/msg/Odometry"},
    {kStdoutTopic, "std_msgs/msg/String"},
  };
  return topics;
}

}  // namespace

namespace go2_monitor_cpp {

ZenohMonitor::ZenohMonitor(
  std::shared_ptr<WebSocketHub> ws_hub,
  std::string endpoint,
  std::string keyexpr
)
: ws_hub_(std::move(ws_hub)),
  endpoint_(std::move(endpoint)),
  keyexpr_(std::move(keyexpr)) {}

void ZenohMonitor::stop() {
  stop_requested_.store(true);
  stop_ros_fallback();
}

void ZenohMonitor::set_error(std::string error) {
  std::lock_guard<std::mutex> lock(mutex_);
  last_error_ = std::move(error);
}

void ZenohMonitor::clear_error() {
  std::lock_guard<std::mutex> lock(mutex_);
  last_error_.clear();
}

void ZenohMonitor::update_rgb(sensor_msgs::msg::CompressedImage image, std::string timestamp) {
  std::lock_guard<std::mutex> lock(mutex_);
  latest_rgb_ = std::move(image);
  latest_rgb_timestamp_ = std::move(timestamp);
  has_rgb_ = true;
  pointing_preview_active_ = false;
  awaiting_live_rgb_after_pointing_ = false;
  rgb_stale_after_pointing_ = false;
  latest_rgb_preview_mime_type_.clear();
  latest_rgb_preview_bytes_.clear();
  last_error_.clear();
  ++revision_;
  ++rgb_revision_;
}

void ZenohMonitor::append_trajectory(TrajectoryPoint point) {
  std::lock_guard<std::mutex> lock(mutex_);
  trajectory_.push_back(std::move(point));
  last_error_.clear();
  ++revision_;
}

void ZenohMonitor::append_stdout(StdoutEntry entry) {
  std::lock_guard<std::mutex> lock(mutex_);
  stdout_entries_.push_back(std::move(entry));
  last_error_.clear();
  ++revision_;
}

bool ZenohMonitor::has_live_data() const {
  std::lock_guard<std::mutex> lock(mutex_);
  return has_rgb_ || pointing_preview_active_ || !trajectory_.empty() || !stdout_entries_.empty();
}

void ZenohMonitor::ensure_ros_fallback_started() {
  std::lock_guard<std::mutex> lock(mutex_);
  if (ros_node_) {
    return;
  }

  if (!rclcpp::ok()) {
    rclcpp::init(0, nullptr);
    owns_rclcpp_context_ = true;
  }

  ros_node_ = std::make_shared<rclcpp::Node>(
    "go2_monitor_fallback_" + std::to_string(reinterpret_cast<std::uintptr_t>(this)));
  ros_executor_ = std::make_unique<rclcpp::executors::SingleThreadedExecutor>();

  rgb_subscription_ = ros_node_->create_subscription<sensor_msgs::msg::CompressedImage>(
    kRgbTopic,
    rclcpp::SensorDataQoS(),
    [this](const sensor_msgs::msg::CompressedImage::SharedPtr message) {
      update_rgb(*message, make_receive_timestamp());
      publish_viewer_update();
    });

  odom_subscription_ = ros_node_->create_subscription<nav_msgs::msg::Odometry>(
    kOdometryTopic,
    rclcpp::SensorDataQoS(),
    [this](const nav_msgs::msg::Odometry::SharedPtr message) {
      const std::string receive_timestamp = make_receive_timestamp();
      TrajectoryPoint point;
      point.timestamp = make_header_timestamp(message->header.stamp, receive_timestamp);
      point.x = message->pose.pose.position.x;
      point.y = message->pose.pose.position.y;

      const auto& orientation = message->pose.pose.orientation;
      const double norm =
        orientation.x * orientation.x +
        orientation.y * orientation.y +
        orientation.z * orientation.z +
        orientation.w * orientation.w;
      if (norm > 1e-12) {
        point.has_yaw = true;
        point.yaw = yaw_from_quaternion(
          orientation.x,
          orientation.y,
          orientation.z,
          orientation.w);
      }

      append_trajectory(std::move(point));
      publish_viewer_update();
    });

  stdout_subscription_ = ros_node_->create_subscription<std_msgs::msg::String>(
    "/" + std::string(kStdoutTopic),
    10,
    [this](const std_msgs::msg::String::SharedPtr message) {
      append_stdout(StdoutEntry{make_receive_timestamp(), message->data});
      publish_viewer_update();
    });

  ros_executor_->add_node(ros_node_);
  ros_spin_thread_ = std::thread([this]() {
    if (ros_executor_) {
      ros_executor_->spin();
    }
  });
}

void ZenohMonitor::stop_ros_fallback() {
  std::thread spin_thread;
  bool shutdown_context = false;

  {
    std::lock_guard<std::mutex> lock(mutex_);
    if (ros_executor_) {
      ros_executor_->cancel();
    }
    spin_thread = std::move(ros_spin_thread_);
  }

  if (spin_thread.joinable()) {
    spin_thread.join();
  }

  {
    std::lock_guard<std::mutex> lock(mutex_);
    stdout_subscription_.reset();
    odom_subscription_.reset();
    rgb_subscription_.reset();
    if (ros_executor_ && ros_node_) {
      ros_executor_->remove_node(ros_node_);
    }
    ros_executor_.reset();
    ros_node_.reset();
    shutdown_context = owns_rclcpp_context_;
    owns_rclcpp_context_ = false;
  }

  if (shutdown_context && rclcpp::ok()) {
    rclcpp::shutdown();
  }
}

void ZenohMonitor::publish_viewer_update() {
  std::uint64_t revision = 0;
  {
    std::lock_guard<std::mutex> lock(mutex_);
    revision = revision_;
  }

  ws_hub_->broadcast(
    "{\"kind\":\"viewer_update\",\"source\":\"zenoh\",\"revision\":" + std::to_string(revision) + "}");
}

void ZenohMonitor::update_pointing_contract_state_locked(std::chrono::steady_clock::time_point now) {
  if (!awaiting_live_rgb_after_pointing_) {
    rgb_stale_after_pointing_ = false;
    return;
  }

  rgb_stale_after_pointing_ = (now - pointing_requested_at_) >= kPointingRgbTimeout;
}

bool ZenohMonitor::handle_sample(const zenoh::Sample& sample) {
  if (sample.get_kind() != Z_SAMPLE_KIND_PUT) {
    return false;
  }

  const auto sample_keyexpr = sample.get_keyexpr().as_string_view();
  const auto topic = classify_topic(sample_keyexpr);
  if (topic == LiveTopic::kUnknown) {
    return false;
  }

  const auto payload = sample.get_payload().as_vector();
  std::string timestamp = make_receive_timestamp();
  std::string error;

  switch (topic) {
    case LiveTopic::kRgb: {
      sensor_msgs::msg::CompressedImage image;
      if (!deserialize_ros_message(payload, image, error)) {
        set_error(
          "failed to deserialize compressed rgb image from " +
          std::string(sample_keyexpr.data(), sample_keyexpr.size()) + ": " + error);
        return false;
      }

      update_rgb(std::move(image), std::move(timestamp));
      return true;
    }
    case LiveTopic::kOdometry: {
      nav_msgs::msg::Odometry odom;
      if (!deserialize_ros_message(payload, odom, error)) {
        set_error(
          "failed to deserialize odometry from " +
          std::string(sample_keyexpr.data(), sample_keyexpr.size()) + ": " + error);
        return false;
      }

      TrajectoryPoint point;
      point.timestamp = make_header_timestamp(odom.header.stamp, timestamp);
      point.x = odom.pose.pose.position.x;
      point.y = odom.pose.pose.position.y;

      const auto& orientation = odom.pose.pose.orientation;
      const double norm =
        orientation.x * orientation.x +
        orientation.y * orientation.y +
        orientation.z * orientation.z +
        orientation.w * orientation.w;
      if (norm > 1e-12) {
        point.has_yaw = true;
        point.yaw = yaw_from_quaternion(
          orientation.x,
          orientation.y,
          orientation.z,
          orientation.w);
      }

      append_trajectory(std::move(point));
      return true;
    }
    case LiveTopic::kStdout: {
      std_msgs::msg::String message;
      if (!deserialize_ros_message(payload, message, error)) {
        set_error(
          "failed to deserialize stdout from " +
          std::string(sample_keyexpr.data(), sample_keyexpr.size()) + ": " + error);
        return false;
      }

      append_stdout(StdoutEntry{std::move(timestamp), std::move(message.data)});
      return true;
    }
    case LiveTopic::kUnknown:
      return false;
  }

  return false;
}

void ZenohMonitor::run() {
  stop_requested_.store(false);
  ensure_ros_fallback_started();
  zenoh::KeyExpr keyexpr(keyexpr_);
  const auto on_sample = [this](const zenoh::Sample& sample) {
    if (handle_sample(sample)) {
      publish_viewer_update();
    }
  };

  while (!stop_requested_.load()) {
    try {
      auto session = zenoh::Session::open(make_session_config(endpoint_));
      auto subscriber = session.declare_subscriber(
        keyexpr,
        on_sample,
        zenoh::closures::none
      );

      clear_error();
      std::cerr << "connected to endpoint " << endpoint_ << std::endl;
      auto next_redeclare = std::chrono::steady_clock::now() + kRedeclareInterval;

      while (!stop_requested_.load()) {
        const auto now = std::chrono::steady_clock::now();
        if (!has_live_data() && now >= next_redeclare) {
          std::move(subscriber).undeclare();
          subscriber = session.declare_subscriber(
            keyexpr,
            on_sample,
            zenoh::closures::none
          );
          next_redeclare = now + kRedeclareInterval;
          continue;
        }
        std::this_thread::sleep_for(kLoopSleep);
      }

      std::move(subscriber).undeclare();
      session.close();
      return;
    } catch (const zenoh::ZException& ex) {
      if (ex.e != Z_ENETWORK) {
        throw;
      }

      const std::string wait_message =
        "waiting for endpoint " + endpoint_ + ", retrying in 1s: " + ex.what();
      set_error(wait_message);
      std::cerr << wait_message << std::endl;
    }

    for (auto waited = std::chrono::milliseconds::zero();
         waited < kEndpointRetryDelay && !stop_requested_.load();
         waited += kLoopSleep) {
      std::this_thread::sleep_for(kLoopSleep);
    }
  }
}

bool ZenohMonitor::list_topics(std::vector<TopicInfo>& topics) {
  topics = live_topics();
  return true;
}

bool ZenohMonitor::get_viewer_snapshot(ViewerSnapshot& snapshot) {
  snapshot = ViewerSnapshot{};
  snapshot.source = source_label();
  snapshot.source_mode = "zenoh";
  snapshot.supports_playback = false;
  snapshot.rgb_topic = kRgbTopic;
  snapshot.depth_topic.clear();
  snapshot.stdout_topic = kStdoutTopic;

  std::lock_guard<std::mutex> lock(mutex_);
  update_pointing_contract_state_locked(std::chrono::steady_clock::now());
  snapshot.revision = revision_;
  snapshot.rgb_revision = rgb_revision_;
  snapshot.pointing_preview_active = pointing_preview_active_;
  snapshot.awaiting_live_rgb_after_pointing = awaiting_live_rgb_after_pointing_;
  snapshot.rgb_stale_after_pointing = rgb_stale_after_pointing_;
  snapshot.trajectory = trajectory_;
  snapshot.stdout_entries = stdout_entries_;

  if (has_rgb_ || pointing_preview_active_) {
    ViewerFrameInfo frame;
    frame.index = 0;
    frame.rgb_revision = rgb_revision_;
    snapshot.frames.push_back(std::move(frame));

    PlaybackTimelineEntry entry;
    entry.index = 0;
    entry.viewer_frame_index = 0;

    if (!latest_rgb_timestamp_.empty()) {
      entry.timestamp = latest_rgb_timestamp_;
    }

    if (!trajectory_.empty()) {
      const auto& point = trajectory_.back();
      entry.has_odom = true;
      entry.odom_index = trajectory_.size() - 1;
      entry.odom_timestamp = point.timestamp;
      entry.odom_x = point.x;
      entry.odom_y = point.y;
    }

    if (!stdout_entries_.empty()) {
      entry.has_stdout = true;
      entry.stdout_index = stdout_entries_.size() - 1;
    }

    snapshot.timeline.push_back(std::move(entry));
  }

  return true;
}

bool ZenohMonitor::render_viewer_image(
  std::size_t index,
  const std::string& stream,
  std::string& mime_type,
  std::string& image_bytes) {
  if (index != 0) {
    std::lock_guard<std::mutex> lock(mutex_);
    last_error_ = "live viewer exposes only the latest frame";
    return false;
  }

  sensor_msgs::msg::CompressedImage rgb_image;
  {
    std::lock_guard<std::mutex> lock(mutex_);
    if (stream == "rgb") {
      if (!has_rgb_) {
        last_error_ = "rgb stream is not available yet";
        return false;
      }
      rgb_image = latest_rgb_;
    } else {
      last_error_ = "zenoh viewer stream must be rgb";
      return false;
    }
  }

  std::string error;
  const bool ok = render_compressed_image_message(rgb_image, mime_type, image_bytes, error);
  if (!ok) {
    std::lock_guard<std::mutex> lock(mutex_);
    last_error_ = error;
    return false;
  }

  {
    std::lock_guard<std::mutex> lock(mutex_);
    last_error_.clear();
  }
  return true;
}

bool ZenohMonitor::accept_pointing_preview(
  const std::string& mime_type,
  const std::string& image_bytes) {
  if ((mime_type != "image/jpeg" && mime_type != "image/png") || image_bytes.empty()) {
    return false;
  }

  {
    std::lock_guard<std::mutex> lock(mutex_);
    latest_rgb_preview_mime_type_.clear();
    latest_rgb_preview_bytes_.clear();
    pointing_preview_active_ = false;
    awaiting_live_rgb_after_pointing_ = true;
    rgb_stale_after_pointing_ = false;
    pointing_requested_at_ = std::chrono::steady_clock::now();
    last_error_.clear();
    ++revision_;
  }

  publish_viewer_update();
  return true;
}

std::string ZenohMonitor::source_label() const {
  return "zenoh:" + endpoint_ + " (" + keyexpr_ + ")";
}

std::string ZenohMonitor::source_mode() const {
  return "zenoh";
}

std::string ZenohMonitor::last_error() const {
  std::lock_guard<std::mutex> lock(mutex_);
  return last_error_;
}

}  // namespace go2_monitor_cpp
