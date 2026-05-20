#pragma once

#include <cstdint>
#include <memory>
#include <mutex>
#include <string>
#include <thread>

namespace go2_monitor_cpp {

class ViewerDataSource;
class WebSocketHub;
class WebServer;
class ZenohMonitor;

struct MonitorRunnerOptions {
  std::string source = "zenoh";
  std::string endpoint = "udp/127.0.0.1:7447";
  std::string keyexpr = "**";
  std::uint16_t port = 8080;
};

class MonitorRunner {
public:
  explicit MonitorRunner(MonitorRunnerOptions options = {});
  ~MonitorRunner();

  MonitorRunner(const MonitorRunner&) = delete;
  MonitorRunner& operator=(const MonitorRunner&) = delete;

  void start();
  void stop();
  void join();
  bool is_running() const;

private:
  void initialize_locked();
  void cleanup_locked();

  MonitorRunnerOptions options_;
  std::shared_ptr<WebSocketHub> ws_hub_;
  std::shared_ptr<ViewerDataSource> viewer_data_source_;
  std::shared_ptr<ZenohMonitor> zenoh_monitor_;
  std::unique_ptr<WebServer> server_;
  std::thread source_thread_;
  std::thread server_thread_;
  mutable std::mutex mutex_;
  bool started_ = false;
  bool running_ = false;
  std::exception_ptr server_exception_;
};

std::shared_ptr<MonitorRunner> start_monitor_background(const MonitorRunnerOptions& options);
int run_monitor_server(const MonitorRunnerOptions& options);

}  // namespace go2_monitor_cpp
