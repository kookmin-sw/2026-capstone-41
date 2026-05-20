#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
cleanup() {
    rm -rf "$tmp_dir"
}
trap cleanup EXIT

echo "Device summary"
rs-enumerate-devices -s
echo

cat > "$tmp_dir/realsense_only_test.cpp" <<'CPP'
#include <atomic>
#include <chrono>
#include <iostream>
#include <thread>

#include <librealsense2/rs.hpp>

using clock_type = std::chrono::steady_clock;

template <typename Fn>
void run_test(const char* name, Fn fn)
{
    try
    {
        fn();
    }
    catch (const rs2::error& e)
    {
        std::cout << name << ": ERROR " << e.what() << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cout << name << ": ERROR " << e.what() << std::endl;
    }
}

int test_ir_only()
{
    rs2::pipeline pipe;
    rs2::config cfg;
    cfg.enable_stream(RS2_STREAM_INFRARED, 1, 640, 480, RS2_FORMAT_Y8, 30);
    cfg.enable_stream(RS2_STREAM_INFRARED, 2, 640, 480, RS2_FORMAT_Y8, 30);

    pipe.start(cfg);

    int frameset_count = 0;
    auto deadline = clock_type::now() + std::chrono::seconds(3);
    while (clock_type::now() < deadline)
    {
        rs2::frameset fs;
        if (pipe.poll_for_frames(&fs))
            frameset_count++;
    }

    pipe.stop();
    std::cout << "IR-only: frameset_count=" << frameset_count << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(300));
    return 0;
}

int test_imu_only()
{
    rs2::pipeline pipe;
    rs2::config cfg;
    cfg.enable_stream(RS2_STREAM_ACCEL, RS2_FORMAT_MOTION_XYZ32F);
    cfg.enable_stream(RS2_STREAM_GYRO, RS2_FORMAT_MOTION_XYZ32F);

    std::atomic<int> gyro_count(0);
    std::atomic<int> accel_count(0);

    auto callback = [&](const rs2::frame& frame)
    {
        if (rs2::motion_frame mf = frame.as<rs2::motion_frame>())
        {
            const auto name = mf.get_profile().stream_name();
            if (name == "Gyro")
                gyro_count.fetch_add(1, std::memory_order_relaxed);
            else if (name == "Accel")
                accel_count.fetch_add(1, std::memory_order_relaxed);
        }
    };

    pipe.start(cfg, callback);
    std::this_thread::sleep_for(std::chrono::seconds(3));
    pipe.stop();

    std::cout
        << "IMU-only: gyro_count=" << gyro_count.load(std::memory_order_relaxed)
        << " accel_count=" << accel_count.load(std::memory_order_relaxed)
        << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(300));
    return 0;
}

int test_ir_imu()
{
    rs2::pipeline pipe;
    rs2::config cfg;
    cfg.enable_stream(RS2_STREAM_INFRARED, 1, 640, 480, RS2_FORMAT_Y8, 30);
    cfg.enable_stream(RS2_STREAM_INFRARED, 2, 640, 480, RS2_FORMAT_Y8, 30);
    cfg.enable_stream(RS2_STREAM_ACCEL, RS2_FORMAT_MOTION_XYZ32F);
    cfg.enable_stream(RS2_STREAM_GYRO, RS2_FORMAT_MOTION_XYZ32F);

    std::atomic<int> frameset_count(0);
    std::atomic<int> gyro_count(0);
    std::atomic<int> accel_count(0);

    auto callback = [&](const rs2::frame& frame)
    {
        if (frame.as<rs2::frameset>())
        {
            frameset_count.fetch_add(1, std::memory_order_relaxed);
            return;
        }

        if (rs2::motion_frame mf = frame.as<rs2::motion_frame>())
        {
            const auto name = mf.get_profile().stream_name();
            if (name == "Gyro")
                gyro_count.fetch_add(1, std::memory_order_relaxed);
            else if (name == "Accel")
                accel_count.fetch_add(1, std::memory_order_relaxed);
        }
    };

    pipe.start(cfg, callback);
    std::this_thread::sleep_for(std::chrono::seconds(5));
    pipe.stop();

    std::cout
        << "IR+IMU: frameset_count=" << frameset_count.load(std::memory_order_relaxed)
        << " gyro_count=" << gyro_count.load(std::memory_order_relaxed)
        << " accel_count=" << accel_count.load(std::memory_order_relaxed)
        << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(300));
    return 0;
}

int main()
{
    rs2::context ctx;
    if (ctx.query_devices().size() == 0)
    {
        std::cerr << "No RealSense device connected" << std::endl;
        return 2;
    }

    run_test("IR-only", test_ir_only);
    run_test("IMU-only", test_imu_only);
    run_test("IR+IMU", test_ir_imu);
    return 0;
}
CPP

g++ -std=c++17 "$tmp_dir/realsense_only_test.cpp" -o "$tmp_dir/realsense_only_test" $(pkg-config --cflags --libs realsense2)
"$tmp_dir/realsense_only_test"
