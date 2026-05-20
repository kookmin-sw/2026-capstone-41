#include "go2_monitor_cpp/monitor_runner.hpp"

#include "go2_monitor_cpp/log_db_reader.hpp"
#include "go2_monitor_cpp/web_server.hpp"
#include "go2_monitor_cpp/zenoh_monitor.hpp"

#include <algorithm>
#include <exception>
#include <filesystem>
#include <fstream>
#include <memory>
#include <sstream>
#include <string>
#include <thread>
#include <vector>

namespace {

std::string build_local_message(const std::string& source_path) {
  namespace fs = std::filesystem;

  if (source_path.empty()) {
    return "local error: --source is empty";
  }

  fs::path path(source_path);
  if (!fs::exists(path)) {
    return "local error: source not found: " + source_path;
  }

  if (fs::is_regular_file(path)) {
    if (path.extension() == ".db") {
      go2_monitor_cpp::LogDbReader reader(source_path);
      if (!reader.is_open()) {
        return "local db error: failed to open " + reader.db_path() + ": " + reader.last_error();
      }
      return "local db opened: " + reader.db_path();
    }

    std::ifstream ifs(path);
    if (!ifs) {
      return "local error: failed to open file: " + source_path;
    }

    std::ostringstream oss;
    oss << ifs.rdbuf();
    const auto content = oss.str();
    return content.empty() ? "local file is empty: " + source_path : content;
  }

  if (fs::is_directory(path)) {
    std::vector<std::string> names;
    for (const auto& entry : fs::directory_iterator(path)) {
      names.push_back(entry.path().filename().string());
    }
    std::sort(names.begin(), names.end());

    std::ostringstream oss;
    oss << "directory: " << source_path;
    if (names.empty()) {
      oss << "\n(empty)";
      return oss.str();
    }
    for (const auto& name : names) {
      oss << "\n" << name;
    }
    return oss.str();
  }

  return "local error: unsupported source type: " + source_path;
}

}  // namespace

namespace go2_monitor_cpp {

MonitorRunner::MonitorRunner(MonitorRunnerOptions options)
: options_(std::move(options)) {}

MonitorRunner::~MonitorRunner() {
  stop();
  try {
    join();
  } catch (...) {
  }
}

void MonitorRunner::initialize_locked() {
  ws_hub_ = std::make_shared<WebSocketHub>();
  viewer_data_source_.reset();
  zenoh_monitor_.reset();

  std::string initial_ws_message;
  if (options_.source == "zenoh") {
    zenoh_monitor_ = std::make_shared<ZenohMonitor>(ws_hub_, options_.endpoint, options_.keyexpr);
    viewer_data_source_ = zenoh_monitor_;
  } else {
    initial_ws_message = build_local_message(options_.source);
    if (std::filesystem::path(options_.source).extension() == ".db") {
      viewer_data_source_ = std::make_shared<LogDbReader>(options_.source);
    }
  }

  server_ = std::make_unique<WebServer>(ws_hub_, viewer_data_source_, std::move(initial_ws_message));
  server_exception_ = nullptr;
}

void MonitorRunner::cleanup_locked() {
  server_.reset();
  zenoh_monitor_.reset();
  viewer_data_source_.reset();
  ws_hub_.reset();
}

void MonitorRunner::start() {
  std::lock_guard<std::mutex> lock(mutex_);
  if (started_) {
    return;
  }

  initialize_locked();

  auto zenoh_monitor = zenoh_monitor_;
  if (zenoh_monitor) {
    source_thread_ = std::thread([zenoh_monitor]() {
      zenoh_monitor->run();
    });
  }

  auto* server = server_.get();
  const std::uint16_t port = options_.port;
  server_thread_ = std::thread([this, server, zenoh_monitor, port]() {
    {
      std::lock_guard<std::mutex> lock(mutex_);
      running_ = true;
    }

    try {
      server->run(port);
    } catch (...) {
      std::lock_guard<std::mutex> lock(mutex_);
      server_exception_ = std::current_exception();
    }

    if (zenoh_monitor) {
      zenoh_monitor->stop();
    }

    std::lock_guard<std::mutex> lock(mutex_);
    running_ = false;
  });

  started_ = true;
}

void MonitorRunner::stop() {
  std::shared_ptr<ZenohMonitor> zenoh_monitor;
  WebServer* server = nullptr;

  {
    std::lock_guard<std::mutex> lock(mutex_);
    if (!started_) {
      return;
    }
    zenoh_monitor = zenoh_monitor_;
    server = server_.get();
  }

  if (zenoh_monitor) {
    zenoh_monitor->stop();
  }
  if (server) {
    server->stop();
  }
}

void MonitorRunner::join() {
  std::thread server_thread;
  std::thread source_thread;
  std::exception_ptr server_exception;

  {
    std::lock_guard<std::mutex> lock(mutex_);
    if (!started_) {
      return;
    }
    server_thread = std::move(server_thread_);
    source_thread = std::move(source_thread_);
  }

  if (server_thread.joinable()) {
    server_thread.join();
  }
  if (source_thread.joinable()) {
    source_thread.join();
  }

  {
    std::lock_guard<std::mutex> lock(mutex_);
    started_ = false;
    running_ = false;
    server_exception = server_exception_;
    server_exception_ = nullptr;
    cleanup_locked();
  }

  if (server_exception) {
    std::rethrow_exception(server_exception);
  }
}

bool MonitorRunner::is_running() const {
  std::lock_guard<std::mutex> lock(mutex_);
  return running_;
}

std::shared_ptr<MonitorRunner> start_monitor_background(const MonitorRunnerOptions& options) {
  auto runner = std::make_shared<MonitorRunner>(options);
  runner->start();
  return runner;
}

int run_monitor_server(const MonitorRunnerOptions& options) {
  MonitorRunner runner(options);
  runner.start();
  runner.join();
  return 0;
}

}  // namespace go2_monitor_cpp
