#pragma once

#include <rclcpp/serialization.hpp>
#include <rclcpp/serialized_message.hpp>

#include <cmath>
#include <cstdint>
#include <cstring>
#include <exception>
#include <string>
#include <vector>

namespace go2_monitor_cpp {

template <typename MessageT>
bool deserialize_ros_message(
  const std::vector<std::uint8_t>& bytes,
  MessageT& message,
  std::string& error) {
  try {
    rclcpp::SerializedMessage serialized(bytes.size());
    auto& serialized_buffer = serialized.get_rcl_serialized_message();
    serialized_buffer.buffer_length = bytes.size();
    std::memcpy(serialized_buffer.buffer, bytes.data(), bytes.size());

    rclcpp::Serialization<MessageT> serializer;
    serializer.deserialize_message(&serialized, &message);
    return true;
  } catch (const std::exception& ex) {
    error = ex.what();
    return false;
  }
}

inline double yaw_from_quaternion(double qx, double qy, double qz, double qw) {
  return std::atan2(
    2.0 * (qw * qz + qx * qy),
    1.0 - 2.0 * (qy * qy + qz * qz));
}

}  // namespace go2_monitor_cpp
