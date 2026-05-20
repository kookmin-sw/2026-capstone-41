#pragma once

#include <crow.h>
#include <cstdint>
#include <memory>
#include <mutex>
#include <string>
#include <unordered_set>

namespace go2_monitor_cpp {

class ViewerDataSource;

class WebSocketHub {
public:
  void add(crow::websocket::connection* conn);
  void remove(crow::websocket::connection* conn);
  void broadcast(const std::string& msg);

private:
  std::mutex mutex_;
  std::unordered_set<crow::websocket::connection*> conns_;
};

class WebServer {
public:
  WebServer(
    std::shared_ptr<WebSocketHub> ws_hub,
    std::shared_ptr<ViewerDataSource> viewer_data_source = nullptr,
    std::string initial_ws_message = {});

  void run(uint16_t port);
  void stop();

private:
  void setup_routes();
  std::string index_html() const;

  std::shared_ptr<WebSocketHub> ws_hub_;
  std::shared_ptr<ViewerDataSource> viewer_data_source_;
  std::string initial_ws_message_;
  crow::SimpleApp app_;
};

}  // namespace go2_monitor_cpp
