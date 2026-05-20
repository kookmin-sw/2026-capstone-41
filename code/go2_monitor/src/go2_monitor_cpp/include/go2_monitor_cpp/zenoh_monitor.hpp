#pragma once

#include "go2_monitor_cpp/viewer_data_source.hpp"

#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/compressed_image.hpp>

#include <atomic>
#include <chrono>
#include <memory>
#include <mutex>
#include <string>
#include <thread>

namespace go2_monitor_cpp {

class WebSocketHub;

}  // namespace go2_monitor_cpp

namespace zenoh {

class Sample;

}  // namespace zenoh

namespace go2_monitor_cpp {

class ZenohMonitor : public ViewerDataSource {
public:
  explicit ZenohMonitor(
    std::shared_ptr<WebSocketHub> ws_hub,
    std::string endpoint = "udp/127.0.0.1:7447",
    std::string keyexpr = "**"
  );

  void run();
  void stop();
  bool list_topics(std::vector<TopicInfo>& topics) override;
  bool get_viewer_snapshot(ViewerSnapshot& snapshot) override;
  bool render_viewer_image(
    std::size_t index,
    const std::string& stream,
    std::string& mime_type,
    std::string& image_bytes) override;
  bool accept_pointing_preview(
    const std::string& mime_type,
    const std::string& image_bytes) override;
  std::string source_label() const override;
  std::string source_mode() const override;
  std::string last_error() const override;

private:
  void set_error(std::string error);
  void clear_error();
  void update_rgb(sensor_msgs::msg::CompressedImage image, std::string timestamp);
  void append_trajectory(TrajectoryPoint point);
  void append_stdout(StdoutEntry entry);
  bool has_live_data() const;
  void ensure_ros_fallback_started();
  void stop_ros_fallback();
  bool handle_sample(const zenoh::Sample& sample);
  void publish_viewer_update();
  void update_pointing_contract_state_locked(std::chrono::steady_clock::time_point now);

  std::shared_ptr<WebSocketHub> ws_hub_;
  std::string endpoint_;
  std::string keyexpr_;
  mutable std::mutex mutex_;
  sensor_msgs::msg::CompressedImage latest_rgb_;
  bool has_rgb_ = false;
  bool pointing_preview_active_ = false;
  bool awaiting_live_rgb_after_pointing_ = false;
  bool rgb_stale_after_pointing_ = false;
  std::string latest_rgb_timestamp_;
  std::string latest_rgb_preview_mime_type_;
  std::string latest_rgb_preview_bytes_;
  std::vector<TrajectoryPoint> trajectory_;
  std::vector<StdoutEntry> stdout_entries_;
  std::string last_error_;
  std::uint64_t revision_ = 0;
  std::uint64_t rgb_revision_ = 0;
  std::chrono::steady_clock::time_point pointing_requested_at_ {};
  std::atomic_bool stop_requested_ = false;
  bool owns_rclcpp_context_ = false;
  rclcpp::Node::SharedPtr ros_node_;
  std::unique_ptr<rclcpp::executors::SingleThreadedExecutor> ros_executor_;
  rclcpp::SubscriptionBase::SharedPtr rgb_subscription_;
  rclcpp::SubscriptionBase::SharedPtr odom_subscription_;
  rclcpp::SubscriptionBase::SharedPtr stdout_subscription_;
  std::thread ros_spin_thread_;
};

}  // namespace go2_monitor_cpp
