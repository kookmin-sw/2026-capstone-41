#pragma once

#include "go2_monitor_cpp/viewer_data_source.hpp"

#include <cstdint>
#include <mutex>
#include <string>
#include <vector>

struct sqlite3;

namespace go2_monitor_cpp {

class LogDbReader : public ViewerDataSource {
public:
  explicit LogDbReader(std::string db_path);
  ~LogDbReader();

  LogDbReader(const LogDbReader&) = delete;
  LogDbReader& operator=(const LogDbReader&) = delete;
  LogDbReader(LogDbReader&&) = delete;
  LogDbReader& operator=(LogDbReader&&) = delete;

  bool is_open() const;
  bool list_topics(std::vector<TopicInfo>& topics) override;
  bool get_viewer_snapshot(ViewerSnapshot& snapshot) override;
  bool render_viewer_image(
    std::size_t index,
    const std::string& stream,
    std::string& mime_type,
    std::string& image_bytes) override;

  const std::string& db_path() const;
  std::string source_label() const override;
  std::string source_mode() const override;
  std::string last_error() const override;

private:
  struct ImageRecord {
    std::string timestamp;
    std::string resolved_path;
  };

  struct SyncedImageRecord {
    ImageRecord rgb;
    ImageRecord depth;
  };

  bool list_trajectory(std::vector<TrajectoryPoint>& points);
  bool list_stdout_entries(std::vector<StdoutEntry>& entries);
  bool list_viewer_frames(std::vector<ViewerFrameInfo>& frames);
  bool list_playback_timeline(std::vector<PlaybackTimelineEntry>& timeline);
  bool ensure_open_locked();
  bool ensure_topics_cache_locked();
  bool ensure_image_pairs_cache_locked();
  bool ensure_trajectory_cache_locked();
  bool ensure_stdout_cache_locked();
  bool ensure_timeline_cache_locked();
  void clear_cache_locked();
  void open_read_only();
  void close();

  mutable std::mutex mutex_;
  sqlite3* db_ = nullptr;
  std::string db_path_;
  std::string last_error_;
  bool topics_cached_ = false;
  bool image_pairs_cached_ = false;
  bool trajectory_cached_ = false;
  bool stdout_cached_ = false;
  bool timeline_cached_ = false;
  std::vector<TopicInfo> topics_cache_;
  std::vector<SyncedImageRecord> image_pairs_cache_;
  std::vector<ViewerFrameInfo> frames_cache_;
  std::vector<TrajectoryPoint> trajectory_cache_;
  std::vector<StdoutEntry> stdout_cache_;
  std::vector<PlaybackTimelineEntry> timeline_cache_;
};

}  // namespace go2_monitor_cpp
