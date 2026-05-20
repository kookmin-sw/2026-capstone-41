#pragma once

#include <sensor_msgs/msg/compressed_image.hpp>
#include <sensor_msgs/msg/image.hpp>

#include <cstddef>
#include <cstdint>
#include <string>
#include <vector>

namespace go2_monitor_cpp {

struct TopicInfo {
  std::string name;
  std::string type;
};

struct ViewerFrameInfo {
  std::size_t index = 0;
  std::uint64_t rgb_revision = 0;
  std::uint64_t depth_revision = 0;
};

struct PlaybackTimelineEntry {
  std::size_t index = 0;
  std::size_t viewer_frame_index = 0;
  std::string timestamp;
  bool has_odom = false;
  std::size_t odom_index = 0;
  std::string odom_timestamp;
  double odom_x = 0.0;
  double odom_y = 0.0;
  bool has_stdout = false;
  std::size_t stdout_index = 0;
};

struct TrajectoryPoint {
  std::string timestamp;
  double x = 0.0;
  double y = 0.0;
  bool has_yaw = false;
  double yaw = 0.0;
};

struct StdoutEntry {
  std::string timestamp;
  std::string message;
};

struct ViewerSnapshot {
  std::string source;
  std::string source_mode;
  bool supports_playback = false;
  std::string rgb_topic = "/camera/color/image_raw";
  std::string depth_topic = "/camera/aligned_depth_to_color/image_raw";
  std::string stdout_topic = "print";
  std::uint64_t revision = 0;
  std::uint64_t rgb_revision = 0;
  std::uint64_t depth_revision = 0;
  bool pointing_preview_active = false;
  bool awaiting_live_rgb_after_pointing = false;
  bool rgb_stale_after_pointing = false;
  std::vector<ViewerFrameInfo> frames;
  std::vector<PlaybackTimelineEntry> timeline;
  std::vector<TrajectoryPoint> trajectory;
  std::vector<StdoutEntry> stdout_entries;
};

class ViewerDataSource {
public:
  virtual ~ViewerDataSource() = default;

  virtual bool list_topics(std::vector<TopicInfo>& topics) = 0;
  virtual bool get_viewer_snapshot(ViewerSnapshot& snapshot) = 0;
  virtual bool render_viewer_image(
    std::size_t index,
    const std::string& stream,
    std::string& mime_type,
    std::string& image_bytes) = 0;
  virtual bool accept_pointing_preview(
    const std::string& mime_type,
    const std::string& image_bytes) {
    (void)mime_type;
    (void)image_bytes;
    return false;
  }

  virtual std::string source_label() const = 0;
  virtual std::string source_mode() const = 0;
  virtual std::string last_error() const = 0;
};

bool render_image_message(
  const sensor_msgs::msg::Image& image,
  const std::string& stream,
  std::string& mime_type,
  std::string& image_bytes,
  std::string& error);

bool render_compressed_image_message(
  const sensor_msgs::msg::CompressedImage& image,
  std::string& mime_type,
  std::string& image_bytes,
  std::string& error);

}  // namespace go2_monitor_cpp
