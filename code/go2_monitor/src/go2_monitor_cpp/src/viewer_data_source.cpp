#include "go2_monitor_cpp/viewer_data_source.hpp"
#include "go2_monitor_cpp/message_utils.hpp"

#include <sensor_msgs/msg/compressed_image.hpp>

#include <jpeglib.h>
#include <png.h>

#include <algorithm>
#include <csetjmp>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <exception>
#include <limits>
#include <cctype>
#include <string>
#include <vector>

namespace {

struct JpegErrorManager {
  jpeg_error_mgr pub;
  jmp_buf jump_buffer;
  char message[JMSG_LENGTH_MAX];
};

void on_jpeg_error(j_common_ptr cinfo) {
  auto* error_manager = reinterpret_cast<JpegErrorManager*>(cinfo->err);
  (*cinfo->err->format_message)(cinfo, error_manager->message);
  longjmp(error_manager->jump_buffer, 1);
}

bool validate_image_layout(
  const sensor_msgs::msg::Image& image,
  std::size_t expected_step,
  const char* stream_name,
  std::string& error) {
  if (image.step < expected_step) {
    error = std::string("invalid image step for ") + stream_name + " stream";
    return false;
  }

  const std::size_t height = static_cast<std::size_t>(image.height);
  if (height == 0) {
    return true;
  }

  const std::size_t required_size = (height - 1) * image.step + expected_step;
  if (image.data.size() < required_size) {
    error = std::string("image data buffer is smaller than declared ") + stream_name + " layout";
    return false;
  }

  return true;
}

bool extract_rgb_pixels(
  const sensor_msgs::msg::Image& image,
  std::vector<std::uint8_t>& rgb_pixels,
  std::string& error) {
  const bool is_rgb8 = image.encoding == "rgb8";
  const bool is_bgr8 = image.encoding == "bgr8";
  const bool is_rgba8 = image.encoding == "rgba8";
  const bool is_bgra8 = image.encoding == "bgra8";

  if (!is_rgb8 && !is_bgr8 && !is_rgba8 && !is_bgra8) {
    error = "unsupported rgb image encoding: " + image.encoding;
    return false;
  }

  const std::size_t channels = (is_rgba8 || is_bgra8) ? 4u : 3u;
  const std::size_t width = static_cast<std::size_t>(image.width);
  const std::size_t height = static_cast<std::size_t>(image.height);
  const std::size_t expected_step = width * channels;
  if (!validate_image_layout(image, expected_step, "rgb", error)) {
    return false;
  }

  rgb_pixels.resize(width * height * 3u);
  if (rgb_pixels.empty()) {
    return true;
  }

  if (is_rgb8 && image.step == expected_step) {
    std::memcpy(rgb_pixels.data(), image.data.data(), rgb_pixels.size());
    return true;
  }

  for (std::size_t y = 0; y < height; ++y) {
    const auto* src_row = image.data.data() + y * image.step;
    auto* dst_row = rgb_pixels.data() + y * width * 3u;

    if (is_rgb8) {
      std::memcpy(dst_row, src_row, width * 3u);
      continue;
    }

    for (std::size_t x = 0; x < width; ++x) {
      const auto* src = src_row + x * channels;
      auto* dst = dst_row + x * 3u;
      if (is_bgr8 || is_bgra8) {
        dst[0] = src[2];
        dst[1] = src[1];
        dst[2] = src[0];
      } else {
        dst[0] = src[0];
        dst[1] = src[1];
        dst[2] = src[2];
      }
    }
  }

  return true;
}

bool extract_depth_gray_pixels(
  const sensor_msgs::msg::Image& image,
  std::vector<std::uint8_t>& gray_pixels,
  std::string& error) {
  if (image.encoding != "16UC1" && image.encoding != "mono8" && image.encoding != "8UC1") {
    error = "unsupported depth image encoding: " + image.encoding;
    return false;
  }

  const std::size_t bytes_per_pixel = (image.encoding == "16UC1") ? 2u : 1u;
  const std::size_t width = static_cast<std::size_t>(image.width);
  const std::size_t height = static_cast<std::size_t>(image.height);
  const std::size_t expected_step = width * bytes_per_pixel;
  if (!validate_image_layout(image, expected_step, "depth", error)) {
    return false;
  }

  std::uint16_t min_value = std::numeric_limits<std::uint16_t>::max();
  std::uint16_t max_value = 0;

  if (image.encoding == "16UC1") {
    for (std::size_t y = 0; y < height; ++y) {
      const auto* row = image.data.data() + y * image.step;
      for (std::size_t x = 0; x < width; ++x) {
        const auto* src = row + x * 2u;
        const auto value = image.is_bigendian
          ? static_cast<std::uint16_t>(src[0] << 8 | src[1])
          : static_cast<std::uint16_t>(src[0] | (src[1] << 8));
        if (value == 0) {
          continue;
        }
        min_value = std::min(min_value, value);
        max_value = std::max(max_value, value);
      }
    }
  } else {
    min_value = 1;
    max_value = 255;
  }

  if (min_value == std::numeric_limits<std::uint16_t>::max()) {
    min_value = 0;
  }

  gray_pixels.assign(width * height, 0);

  if (image.encoding == "16UC1") {
    for (std::size_t y = 0; y < height; ++y) {
      const auto* row = image.data.data() + y * image.step;
      auto* dst_row = gray_pixels.data() + y * width;
      for (std::size_t x = 0; x < width; ++x) {
        const auto* src = row + x * 2u;
        const auto value = image.is_bigendian
          ? static_cast<std::uint16_t>(src[0] << 8 | src[1])
          : static_cast<std::uint16_t>(src[0] | (src[1] << 8));

        if (value == 0) {
          dst_row[x] = 0;
          continue;
        }

        if (max_value > min_value) {
          const auto numerator = static_cast<std::uint32_t>(value - min_value) * 255u;
          dst_row[x] = static_cast<std::uint8_t>(
            std::min<std::uint32_t>(255u, numerator / (max_value - min_value)));
        } else {
          dst_row[x] = 255;
        }
      }
    }
    return true;
  }

  for (std::size_t y = 0; y < height; ++y) {
    const auto* row = image.data.data() + y * image.step;
    auto* dst_row = gray_pixels.data() + y * width;
    for (std::size_t x = 0; x < width; ++x) {
      const auto value = row[x];
      if (value == 0) {
        dst_row[x] = 0;
        continue;
      }

      const auto numerator = static_cast<std::uint32_t>(value - 1u) * 255u;
      dst_row[x] = static_cast<std::uint8_t>(std::min<std::uint32_t>(255u, numerator / 254u));
    }
  }

  return true;
}

bool encode_rgb_to_jpeg(
  const std::vector<std::uint8_t>& rgb_pixels,
  std::uint32_t width,
  std::uint32_t height,
  std::string& jpeg_bytes,
  std::string& error) {
  if (width == 0 || height == 0) {
    error = "rgb image has invalid size";
    return false;
  }

  jpeg_compress_struct cinfo {};
  JpegErrorManager jerr {};
  cinfo.err = jpeg_std_error(&jerr.pub);
  jerr.pub.error_exit = on_jpeg_error;

  if (setjmp(jerr.jump_buffer)) {
    error = jerr.message;
    jpeg_destroy_compress(&cinfo);
    return false;
  }

  jpeg_create_compress(&cinfo);

  unsigned char* output_buffer = nullptr;
  unsigned long output_size = 0;
  jpeg_mem_dest(&cinfo, &output_buffer, &output_size);

  cinfo.image_width = width;
  cinfo.image_height = height;
  cinfo.input_components = 3;
  cinfo.in_color_space = JCS_RGB;

  jpeg_set_defaults(&cinfo);
  jpeg_set_quality(&cinfo, 90, TRUE);
  jpeg_start_compress(&cinfo, TRUE);

  const std::size_t row_stride = static_cast<std::size_t>(width) * 3u;
  while (cinfo.next_scanline < cinfo.image_height) {
    JSAMPROW row_pointer[1];
    row_pointer[0] = const_cast<JSAMPLE*>(
      rgb_pixels.data() + static_cast<std::size_t>(cinfo.next_scanline) * row_stride);
    jpeg_write_scanlines(&cinfo, row_pointer, 1);
  }

  jpeg_finish_compress(&cinfo);
  jpeg_destroy_compress(&cinfo);

  jpeg_bytes.assign(reinterpret_cast<const char*>(output_buffer), output_size);
  std::free(output_buffer);
  return true;
}

bool encode_gray_to_png(
  const std::vector<std::uint8_t>& gray_pixels,
  std::uint32_t width,
  std::uint32_t height,
  std::string& png_bytes,
  std::string& error) {
  if (width == 0 || height == 0) {
    error = "depth image has invalid size";
    return false;
  }

  png_image image {};
  image.version = PNG_IMAGE_VERSION;
  image.width = width;
  image.height = height;
  image.format = PNG_FORMAT_GRAY;

  png_alloc_size_t size = 0;
  if (!png_image_write_to_memory(&image, nullptr, &size, 0, gray_pixels.data(), 0, nullptr)) {
    error = image.message;
    png_image_free(&image);
    return false;
  }

  png_bytes.resize(size);
  if (!png_image_write_to_memory(&image, png_bytes.data(), &size, 0, gray_pixels.data(), 0, nullptr)) {
    error = image.message;
    png_image_free(&image);
    return false;
  }

  png_bytes.resize(size);
  png_image_free(&image);
  return true;
}

}  // namespace

namespace go2_monitor_cpp {

bool render_image_message(
  const sensor_msgs::msg::Image& image,
  const std::string& stream,
  std::string& mime_type,
  std::string& image_bytes,
  std::string& error) {
  if (stream == "rgb") {
    std::vector<std::uint8_t> rgb_pixels;
    if (!extract_rgb_pixels(image, rgb_pixels, error) ||
        !encode_rgb_to_jpeg(rgb_pixels, image.width, image.height, image_bytes, error)) {
      return false;
    }
    mime_type = "image/jpeg";
    return true;
  }

  if (stream == "depth") {
    std::vector<std::uint8_t> gray_pixels;
    if (!extract_depth_gray_pixels(image, gray_pixels, error) ||
        !encode_gray_to_png(gray_pixels, image.width, image.height, image_bytes, error)) {
      return false;
    }
    mime_type = "image/png";
    return true;
  }

  error = "viewer stream must be rgb or depth";
  return false;
}

bool render_compressed_image_message(
  const sensor_msgs::msg::CompressedImage& image,
  std::string& mime_type,
  std::string& image_bytes,
  std::string& error) {
  std::string format = image.format;
  std::transform(format.begin(), format.end(), format.begin(), [](unsigned char ch) {
    return static_cast<char>(std::tolower(ch));
  });

  if (format.empty() || format.find("jpeg") != std::string::npos || format.find("jpg") != std::string::npos) {
    mime_type = "image/jpeg";
  } else if (format.find("png") != std::string::npos) {
    mime_type = "image/png";
  } else {
    error = "unsupported compressed rgb image format: " + image.format;
    return false;
  }

  image_bytes.assign(reinterpret_cast<const char*>(image.data.data()), image.data.size());
  return true;
}

}  // namespace go2_monitor_cpp
