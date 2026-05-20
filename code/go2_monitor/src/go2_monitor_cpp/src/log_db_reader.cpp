#include "go2_monitor_cpp/log_db_reader.hpp"
#include "go2_monitor_cpp/message_utils.hpp"

#include <sqlite3.h>

#include <algorithm>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <mutex>
#include <string>
#include <utility>
#include <vector>

namespace {

constexpr const char* kImageType = "sensor_msgs/msg/Image";
constexpr const char* kRgbTopic = "/camera/color/image_raw";
constexpr const char* kDepthTopic = "/camera/aligned_depth_to_color/image_raw";
constexpr const char* kOdometryTopic = "/utlidar/robot_odom";
constexpr const char* kOdometryType = "nav_msgs/msg/Odometry";
constexpr const char* kStdoutTopic = "print";
constexpr const char* kStdoutType = "stdout";

struct StoredImageRecord {
  std::int64_t id = 0;
  std::string timestamp;
  std::string stored_path;
  std::string resolved_path;
};

struct SyncedImagePair {
  StoredImageRecord rgb;
  StoredImageRecord depth;
};

std::string decode_json_string(const std::string& value) {
  if (value.size() < 2 || value.front() != '"' || value.back() != '"') {
    return value;
  }

  std::string decoded;
  decoded.reserve(value.size() - 2);

  for (std::size_t i = 1; i + 1 < value.size(); ++i) {
    const char ch = value[i];
    if (ch != '\\' || i + 1 >= value.size() - 1) {
      decoded.push_back(ch);
      continue;
    }

    const char escaped = value[++i];
    switch (escaped) {
      case '\\':
        decoded.push_back('\\');
        break;
      case '"':
        decoded.push_back('"');
        break;
      case '/':
        decoded.push_back('/');
        break;
      case 'b':
        decoded.push_back('\b');
        break;
      case 'f':
        decoded.push_back('\f');
        break;
      case 'n':
        decoded.push_back('\n');
        break;
      case 'r':
        decoded.push_back('\r');
        break;
      case 't':
        decoded.push_back('\t');
        break;
      default:
        decoded.push_back(escaped);
        break;
    }
  }

  return decoded;
}

bool extract_suffix_after_session_dir(
  const std::filesystem::path& path,
  const std::string& session_dir,
  std::filesystem::path& suffix) {
  suffix.clear();
  if (session_dir.empty()) {
    return false;
  }

  bool found_session = false;
  for (const auto& part : path) {
    if (!found_session) {
      if (part.string() == session_dir) {
        found_session = true;
      }
      continue;
    }

    suffix /= part;
  }

  return found_session;
}

std::string resolve_log_path_from_db(const std::string& db_path, const std::string& stored_path) {
  namespace fs = std::filesystem;

  if (stored_path.empty()) {
    return {};
  }

  const fs::path db_dir = fs::path(db_path).parent_path();
  const fs::path stored_fs_path(stored_path);
  const std::string session_dir = db_dir.filename().string();
  fs::path suffix_after_session_dir;
  const bool has_session_dir =
    extract_suffix_after_session_dir(stored_fs_path, session_dir, suffix_after_session_dir);

  if (stored_fs_path.is_relative()) {
    const auto direct_candidate = (db_dir / stored_fs_path).lexically_normal();
    if (fs::exists(direct_candidate)) {
      return direct_candidate.string();
    }

    if (has_session_dir) {
      return (db_dir / suffix_after_session_dir).lexically_normal().string();
    }

    return direct_candidate.string();
  }

  if (fs::exists(stored_fs_path)) {
    return stored_fs_path.string();
  }

  if (has_session_dir) {
    const auto candidate = (db_dir / suffix_after_session_dir).lexically_normal();
    if (fs::exists(candidate)) {
      return candidate.string();
    }
  }

  return (db_dir / stored_fs_path.filename()).lexically_normal().string();
}

bool read_file_bytes(const std::string& path, std::vector<std::uint8_t>& bytes, std::string& error) {
  std::ifstream ifs(path, std::ios::binary);
  if (!ifs) {
    error = "failed to open image file: " + path;
    return false;
  }

  ifs.seekg(0, std::ios::end);
  const auto size = ifs.tellg();
  if (size < 0) {
    error = "failed to read image file size: " + path;
    return false;
  }

  bytes.resize(static_cast<std::size_t>(size));
  ifs.seekg(0, std::ios::beg);
  if (!bytes.empty()) {
    ifs.read(reinterpret_cast<char*>(bytes.data()), static_cast<std::streamsize>(bytes.size()));
  }

  if (!ifs.good() && !ifs.eof()) {
    error = "failed to read image file bytes: " + path;
    return false;
  }

  return true;
}

bool load_image_records_for_topic(
  sqlite3* db,
  const std::string& db_path,
  const char* topic_name,
  std::vector<StoredImageRecord>& records,
  std::string& error) {
  records.clear();

  static constexpr const char* kSql =
    "SELECT id, timestamp, data "
    "FROM logs "
    "WHERE name = ? AND type = ? "
    "ORDER BY timestamp ASC, id ASC";

  sqlite3_stmt* stmt = nullptr;
  const int prepare_rc = sqlite3_prepare_v2(db, kSql, -1, &stmt, nullptr);
  if (prepare_rc != SQLITE_OK) {
    error = sqlite3_errmsg(db);
    return false;
  }

  sqlite3_bind_text(stmt, 1, topic_name, -1, SQLITE_STATIC);
  sqlite3_bind_text(stmt, 2, kImageType, -1, SQLITE_STATIC);

  int step_rc = SQLITE_ROW;
  while ((step_rc = sqlite3_step(stmt)) == SQLITE_ROW) {
    StoredImageRecord record;
    record.id = static_cast<std::int64_t>(sqlite3_column_int64(stmt, 0));

    const auto* timestamp_text = sqlite3_column_text(stmt, 1);
    const auto* data_text = sqlite3_column_text(stmt, 2);

    record.timestamp = timestamp_text != nullptr ? reinterpret_cast<const char*>(timestamp_text) : "";
    record.stored_path = data_text != nullptr ? decode_json_string(reinterpret_cast<const char*>(data_text)) : "";
    record.resolved_path = resolve_log_path_from_db(db_path, record.stored_path);
    records.push_back(std::move(record));
  }

  sqlite3_finalize(stmt);

  if (step_rc != SQLITE_DONE) {
    error = sqlite3_errmsg(db);
    return false;
  }

  return true;
}

bool load_synced_image_pairs(
  sqlite3* db,
  const std::string& db_path,
  std::vector<SyncedImagePair>& pairs,
  std::string& error) {
  std::vector<StoredImageRecord> rgb_records;
  std::vector<StoredImageRecord> depth_records;

  if (!load_image_records_for_topic(db, db_path, kRgbTopic, rgb_records, error)) {
    return false;
  }
  if (!load_image_records_for_topic(db, db_path, kDepthTopic, depth_records, error)) {
    return false;
  }

  const std::size_t total = std::min(rgb_records.size(), depth_records.size());
  if (total == 0) {
    error = "rgb/depth image frames were not found in the current database";
    return false;
  }

  pairs.clear();
  pairs.reserve(total);
  for (std::size_t i = 0; i < total; ++i) {
    pairs.push_back(SyncedImagePair{rgb_records[i], depth_records[i]});
  }

  return true;
}

bool load_trajectory_points(
  sqlite3* db,
  std::vector<go2_monitor_cpp::TrajectoryPoint>& points,
  std::string& error) {
  points.clear();

  static constexpr const char* kSql =
    "SELECT timestamp, "
    "json_extract(data, '$.pose.pose.position.x'), "
    "json_extract(data, '$.pose.pose.position.y'), "
    "json_extract(data, '$.pose.pose.orientation.x'), "
    "json_extract(data, '$.pose.pose.orientation.y'), "
    "json_extract(data, '$.pose.pose.orientation.z'), "
    "json_extract(data, '$.pose.pose.orientation.w') "
    "FROM logs "
    "WHERE name = ? AND type = ? "
    "ORDER BY timestamp ASC, id ASC";

  sqlite3_stmt* stmt = nullptr;
  const int prepare_rc = sqlite3_prepare_v2(db, kSql, -1, &stmt, nullptr);
  if (prepare_rc != SQLITE_OK) {
    error = sqlite3_errmsg(db);
    return false;
  }

  sqlite3_bind_text(stmt, 1, kOdometryTopic, -1, SQLITE_STATIC);
  sqlite3_bind_text(stmt, 2, kOdometryType, -1, SQLITE_STATIC);

  int step_rc = SQLITE_ROW;
  while ((step_rc = sqlite3_step(stmt)) == SQLITE_ROW) {
    if (sqlite3_column_type(stmt, 1) == SQLITE_NULL || sqlite3_column_type(stmt, 2) == SQLITE_NULL) {
      continue;
    }

    go2_monitor_cpp::TrajectoryPoint point;

    const auto* timestamp_text = sqlite3_column_text(stmt, 0);
    point.timestamp = timestamp_text != nullptr ? reinterpret_cast<const char*>(timestamp_text) : "";
    point.x = sqlite3_column_double(stmt, 1);
    point.y = sqlite3_column_double(stmt, 2);

    const bool has_quaternion =
      sqlite3_column_type(stmt, 3) != SQLITE_NULL &&
      sqlite3_column_type(stmt, 4) != SQLITE_NULL &&
      sqlite3_column_type(stmt, 5) != SQLITE_NULL &&
      sqlite3_column_type(stmt, 6) != SQLITE_NULL;
    if (has_quaternion) {
      const double qx = sqlite3_column_double(stmt, 3);
      const double qy = sqlite3_column_double(stmt, 4);
      const double qz = sqlite3_column_double(stmt, 5);
      const double qw = sqlite3_column_double(stmt, 6);
      const double norm = qx * qx + qy * qy + qz * qz + qw * qw;
      if (norm > 1e-12) {
        point.has_yaw = true;
        point.yaw = go2_monitor_cpp::yaw_from_quaternion(qx, qy, qz, qw);
      }
    }

    points.push_back(std::move(point));
  }

  sqlite3_finalize(stmt);

  if (step_rc != SQLITE_DONE) {
    error = sqlite3_errmsg(db);
    return false;
  }

  return true;
}

bool load_stdout_entries(
  sqlite3* db,
  std::vector<go2_monitor_cpp::StdoutEntry>& entries,
  std::string& error) {
  entries.clear();

  static constexpr const char* kSql =
    "SELECT timestamp, "
    "CASE "
    "  WHEN json_valid(data) THEN COALESCE(json_extract(data, '$.message'), json_extract(data, '$'), data) "
    "  ELSE data "
    "END "
    "FROM logs "
    "WHERE name = ? AND type = ? "
    "ORDER BY timestamp ASC, id ASC";

  sqlite3_stmt* stmt = nullptr;
  const int prepare_rc = sqlite3_prepare_v2(db, kSql, -1, &stmt, nullptr);
  if (prepare_rc != SQLITE_OK) {
    error = sqlite3_errmsg(db);
    return false;
  }

  sqlite3_bind_text(stmt, 1, kStdoutTopic, -1, SQLITE_STATIC);
  sqlite3_bind_text(stmt, 2, kStdoutType, -1, SQLITE_STATIC);

  int step_rc = SQLITE_ROW;
  while ((step_rc = sqlite3_step(stmt)) == SQLITE_ROW) {
    if (sqlite3_column_type(stmt, 1) == SQLITE_NULL) {
      continue;
    }

    go2_monitor_cpp::StdoutEntry entry;

    const auto* timestamp_text = sqlite3_column_text(stmt, 0);
    const auto* message_text = sqlite3_column_text(stmt, 1);
    entry.timestamp = timestamp_text != nullptr ? reinterpret_cast<const char*>(timestamp_text) : "";
    entry.message = message_text != nullptr ? reinterpret_cast<const char*>(message_text) : "";
    entries.push_back(std::move(entry));
  }

  sqlite3_finalize(stmt);

  if (step_rc != SQLITE_DONE) {
    error = sqlite3_errmsg(db);
    return false;
  }

  return true;
}

}  // namespace

namespace go2_monitor_cpp {

LogDbReader::LogDbReader(std::string db_path)
: db_path_(std::move(db_path)) {
  open_read_only();
}

LogDbReader::~LogDbReader() {
  close();
}

bool LogDbReader::is_open() const {
  std::lock_guard<std::mutex> lock(mutex_);
  return db_ != nullptr;
}

bool LogDbReader::ensure_open_locked() {
  if (db_ != nullptr) {
    return true;
  }

  last_error_ = "log db is not open";
  return false;
}

void LogDbReader::clear_cache_locked() {
  topics_cached_ = false;
  image_pairs_cached_ = false;
  trajectory_cached_ = false;
  stdout_cached_ = false;
  timeline_cached_ = false;
  topics_cache_.clear();
  image_pairs_cache_.clear();
  frames_cache_.clear();
  trajectory_cache_.clear();
  stdout_cache_.clear();
  timeline_cache_.clear();
}

bool LogDbReader::ensure_topics_cache_locked() {
  if (!ensure_open_locked()) {
    return false;
  }

  if (topics_cached_) {
    return true;
  }

  static constexpr const char* kSql =
    "SELECT name, type "
    "FROM logs "
    "GROUP BY name, type "
    "ORDER BY name ASC, type ASC";

  sqlite3_stmt* stmt = nullptr;
  const int prepare_rc = sqlite3_prepare_v2(db_, kSql, -1, &stmt, nullptr);
  if (prepare_rc != SQLITE_OK) {
    last_error_ = sqlite3_errmsg(db_);
    return false;
  }

  std::vector<TopicInfo> topics;
  int step_rc = SQLITE_ROW;
  while ((step_rc = sqlite3_step(stmt)) == SQLITE_ROW) {
    TopicInfo topic;

    const auto* name_text = sqlite3_column_text(stmt, 0);
    const auto* type_text = sqlite3_column_text(stmt, 1);

    topic.name = name_text != nullptr ? reinterpret_cast<const char*>(name_text) : "";
    topic.type = type_text != nullptr ? reinterpret_cast<const char*>(type_text) : "";
    topics.push_back(std::move(topic));
  }

  sqlite3_finalize(stmt);

  if (step_rc != SQLITE_DONE) {
    last_error_ = sqlite3_errmsg(db_);
    return false;
  }

  topics_cache_ = std::move(topics);
  topics_cached_ = true;
  last_error_.clear();
  return true;
}

bool LogDbReader::ensure_image_pairs_cache_locked() {
  if (!ensure_open_locked()) {
    return false;
  }

  if (image_pairs_cached_) {
    return true;
  }

  std::vector<SyncedImagePair> pairs;
  std::string error;
  if (!load_synced_image_pairs(db_, db_path_, pairs, error)) {
    last_error_ = error;
    return false;
  }

  std::vector<SyncedImageRecord> image_pairs;
  std::vector<ViewerFrameInfo> frames;
  image_pairs.reserve(pairs.size());
  frames.reserve(pairs.size());
  for (std::size_t i = 0; i < pairs.size(); ++i) {
    SyncedImageRecord record;
    record.rgb.timestamp = std::move(pairs[i].rgb.timestamp);
    record.rgb.resolved_path = std::move(pairs[i].rgb.resolved_path);
    record.depth.timestamp = std::move(pairs[i].depth.timestamp);
    record.depth.resolved_path = std::move(pairs[i].depth.resolved_path);
    image_pairs.push_back(std::move(record));

    ViewerFrameInfo frame;
    frame.index = i;
    frames.push_back(frame);
  }

  image_pairs_cache_ = std::move(image_pairs);
  frames_cache_ = std::move(frames);
  image_pairs_cached_ = true;
  last_error_.clear();
  return true;
}

bool LogDbReader::ensure_trajectory_cache_locked() {
  if (!ensure_open_locked()) {
    return false;
  }

  if (trajectory_cached_) {
    return true;
  }

  std::vector<TrajectoryPoint> trajectory;
  std::string error;
  if (!load_trajectory_points(db_, trajectory, error)) {
    last_error_ = error;
    return false;
  }

  trajectory_cache_ = std::move(trajectory);
  trajectory_cached_ = true;
  last_error_.clear();
  return true;
}

bool LogDbReader::ensure_stdout_cache_locked() {
  if (!ensure_open_locked()) {
    return false;
  }

  if (stdout_cached_) {
    return true;
  }

  std::vector<StdoutEntry> stdout_entries;
  std::string error;
  if (!load_stdout_entries(db_, stdout_entries, error)) {
    last_error_ = error;
    return false;
  }

  stdout_cache_ = std::move(stdout_entries);
  stdout_cached_ = true;
  last_error_.clear();
  return true;
}

bool LogDbReader::ensure_timeline_cache_locked() {
  if (timeline_cached_) {
    return true;
  }

  if (!ensure_image_pairs_cache_locked() ||
      !ensure_trajectory_cache_locked() ||
      !ensure_stdout_cache_locked()) {
    return false;
  }

  timeline_cache_.clear();
  timeline_cache_.reserve(image_pairs_cache_.size());

  std::size_t odom_index = 0;
  std::size_t stdout_index = 0;
  for (std::size_t i = 0; i < image_pairs_cache_.size(); ++i) {
    PlaybackTimelineEntry entry;
    entry.index = i;
    entry.viewer_frame_index = i;
    entry.timestamp = image_pairs_cache_[i].rgb.timestamp.empty()
      ? image_pairs_cache_[i].depth.timestamp
      : image_pairs_cache_[i].rgb.timestamp;

    if (!trajectory_cache_.empty()) {
      while (odom_index + 1 < trajectory_cache_.size() &&
             trajectory_cache_[odom_index + 1].timestamp <= entry.timestamp) {
        ++odom_index;
      }

      entry.has_odom = true;
      entry.odom_index = odom_index;
      entry.odom_timestamp = trajectory_cache_[odom_index].timestamp;
      entry.odom_x = trajectory_cache_[odom_index].x;
      entry.odom_y = trajectory_cache_[odom_index].y;
    }

    while (stdout_index < stdout_cache_.size() && stdout_cache_[stdout_index].timestamp <= entry.timestamp) {
      ++stdout_index;
    }
    if (stdout_index > 0) {
      entry.has_stdout = true;
      entry.stdout_index = stdout_index - 1;
    }

    timeline_cache_.push_back(std::move(entry));
  }

  timeline_cached_ = true;
  last_error_.clear();
  return true;
}

bool LogDbReader::list_topics(std::vector<TopicInfo>& topics) {
  std::lock_guard<std::mutex> lock(mutex_);
  if (!ensure_topics_cache_locked()) {
    topics.clear();
    return false;
  }

  topics = topics_cache_;
  last_error_.clear();
  return true;
}

bool LogDbReader::list_trajectory(std::vector<TrajectoryPoint>& points) {
  std::lock_guard<std::mutex> lock(mutex_);
  if (!ensure_trajectory_cache_locked()) {
    points.clear();
    return false;
  }

  points = trajectory_cache_;
  last_error_.clear();
  return true;
}

bool LogDbReader::list_stdout_entries(std::vector<StdoutEntry>& entries) {
  std::lock_guard<std::mutex> lock(mutex_);
  if (!ensure_stdout_cache_locked()) {
    entries.clear();
    return false;
  }

  entries = stdout_cache_;
  last_error_.clear();
  return true;
}

bool LogDbReader::list_viewer_frames(std::vector<ViewerFrameInfo>& frames) {
  std::lock_guard<std::mutex> lock(mutex_);
  if (!ensure_image_pairs_cache_locked()) {
    frames.clear();
    return false;
  }

  frames = frames_cache_;
  last_error_.clear();
  return true;
}

bool LogDbReader::list_playback_timeline(std::vector<PlaybackTimelineEntry>& timeline) {
  std::lock_guard<std::mutex> lock(mutex_);
  if (!ensure_timeline_cache_locked()) {
    timeline.clear();
    return false;
  }

  timeline = timeline_cache_;
  last_error_.clear();
  return true;
}

bool LogDbReader::get_viewer_snapshot(ViewerSnapshot& snapshot) {
  std::lock_guard<std::mutex> lock(mutex_);
  snapshot = ViewerSnapshot{};
  snapshot.source = db_path_;
  snapshot.source_mode = "db";
  snapshot.supports_playback = true;

  if (!ensure_image_pairs_cache_locked() ||
      !ensure_timeline_cache_locked() ||
      !ensure_trajectory_cache_locked() ||
      !ensure_stdout_cache_locked()) {
    return false;
  }

  snapshot.frames = frames_cache_;
  snapshot.timeline = timeline_cache_;
  snapshot.trajectory = trajectory_cache_;
  snapshot.stdout_entries = stdout_cache_;
  last_error_.clear();
  return true;
}

bool LogDbReader::render_viewer_image(
  std::size_t index,
  const std::string& stream,
  std::string& mime_type,
  std::string& image_bytes) {
  bool is_rgb = false;
  std::string resolved_path;
  {
    std::lock_guard<std::mutex> lock(mutex_);
    if (!ensure_image_pairs_cache_locked()) {
      return false;
    }

    is_rgb = stream == "rgb";
    const bool is_depth = stream == "depth";
    if (!is_rgb && !is_depth) {
      last_error_ = "viewer stream must be rgb or depth";
      return false;
    }

    if (index >= image_pairs_cache_.size()) {
      last_error_ = "viewer frame index is out of range";
      return false;
    }

    const auto& record = is_rgb ? image_pairs_cache_[index].rgb : image_pairs_cache_[index].depth;
    resolved_path = record.resolved_path;
  }

  std::vector<std::uint8_t> serialized_bytes;
  std::string error;
  if (!read_file_bytes(resolved_path, serialized_bytes, error)) {
    std::lock_guard<std::mutex> lock(mutex_);
    last_error_ = error;
    return false;
  }

  sensor_msgs::msg::Image image;
  if (!deserialize_ros_message(serialized_bytes, image, error)) {
    std::lock_guard<std::mutex> lock(mutex_);
    last_error_ = "failed to deserialize ROS image: " + error;
    return false;
  }

  if (!render_image_message(image, stream, mime_type, image_bytes, error)) {
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

const std::string& LogDbReader::db_path() const {
  return db_path_;
}

std::string LogDbReader::source_label() const {
  return db_path_;
}

std::string LogDbReader::source_mode() const {
  return "db";
}

std::string LogDbReader::last_error() const {
  std::lock_guard<std::mutex> lock(mutex_);
  return last_error_;
}

void LogDbReader::open_read_only() {
  std::lock_guard<std::mutex> lock(mutex_);

  if (db_path_.empty()) {
    last_error_ = "log db path is empty";
    return;
  }

  sqlite3* db = nullptr;
  const int rc = sqlite3_open_v2(db_path_.c_str(), &db, SQLITE_OPEN_READONLY, nullptr);

  if (rc != SQLITE_OK) {
    if (db != nullptr) {
      last_error_ = sqlite3_errmsg(db);
      sqlite3_close(db);
    } else {
      last_error_ = "failed to open sqlite database";
    }
    return;
  }

  db_ = db;
  clear_cache_locked();
  last_error_.clear();
}

void LogDbReader::close() {
  std::lock_guard<std::mutex> lock(mutex_);

  if (db_ == nullptr) {
    return;
  }

  sqlite3_close(db_);
  db_ = nullptr;
  clear_cache_locked();
}

}  // namespace go2_monitor_cpp
