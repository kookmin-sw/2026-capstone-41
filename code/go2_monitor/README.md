# go2_monitor

ROS 2 Humble 기반 C++ 모니터링 서버다. 실시간 Zenoh 스트림과 SQLite 로그를 같은 웹 UI에서 본다.

주 실행 파일:

```bash
ros2 run go2_monitor_cpp monitor_server
```

## Requirements

- Ubuntu + ROS 2 Humble
- CMake 3.16+, C++17
- `zenoh-c`, `zenoh-cpp` 설치 경로: `$HOME/.local`
- `pybind11`, SQLite3, JPEG, PNG

기본 패키지:

```bash
sudo apt update
sudo apt install -y \
  build-essential cmake ninja-build pkg-config git \
  libasio-dev \
  libsqlite3-dev libjpeg-dev libpng-dev \
  python3-dev python3-pip

python3 -m pip install --user pybind11
```

## Dependencies

Rust:

```bash
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"
rustup update
cargo --version
rustc --version
```

zenoh-c:

```bash
mkdir -p /home/tenstorrent/workspace/go2_monitor/zenoh
cd /home/tenstorrent/workspace/go2_monitor/zenoh
git clone https://github.com/eclipse-zenoh/zenoh-c.git
cd zenoh-c
mkdir -p build
cd build
cmake .. -GNinja -DCMAKE_INSTALL_PREFIX="$HOME/.local"
cmake --build .
cmake --install .
```

zenoh-cpp:

```bash
cd /home/tenstorrent/workspace/go2_monitor/zenoh
git clone https://github.com/eclipse-zenoh/zenoh-cpp.git
cd zenoh-cpp
mkdir -p build
cd build
cmake .. -GNinja -DCMAKE_INSTALL_PREFIX="$HOME/.local"
cmake --build .
cmake --install .
```

## Build

```bash
cd /home/tenstorrent/workspace/go2_monitor
export LD_LIBRARY_PATH="$HOME/.local/lib:$LD_LIBRARY_PATH"
source /opt/ros/humble/setup.bash
colcon build --packages-select go2_monitor_cpp \
  --cmake-args -DCMAKE_PREFIX_PATH="$HOME/.local"
source install/setup.bash
```

주요 산출물:

- `install/go2_monitor_cpp/lib/go2_monitor_cpp/monitor_server`
- Python module: `install/go2_monitor_cpp/local/lib/python*/dist-packages/go2_monitor*.so`

선택 빌드 옵션:

| 옵션 | 기본값 | 설명 |
| --- | --- | --- |
| `-DGO2_MONITOR_BUILD_BENCHMARK=ON` | `OFF` | viewer benchmark server 빌드 |
| `-DGO2_MONITOR_BUILD_PYTHON_DEPLOYMENT=ON` | `OFF` | Python 배포 번들 생성 |

## Run

실시간 Zenoh 스트림:

```bash
ros2 run go2_monitor_cpp monitor_server \
  --source=zenoh \
  --endpoint=tcp/192.168.0.90:7447 \
  --port=8080
```

브라우저:

```text
http://127.0.0.1:8080
```

SQLite 로그 재생:

```bash
ros2 run go2_monitor_cpp monitor_server \
  --source=/path/to/log.db \
  --port=8080
```

## CLI

| 옵션 | 기본값 | 설명 |
| --- | --- | --- |
| `--source=` | `zenoh` | `zenoh` 또는 로컬 경로. `.db`면 로그 뷰어 |
| `--endpoint=` | `udp/127.0.0.1:7447` | Zenoh endpoint. `tcp/...` 또는 `udp/...` scheme이 transport에 반영됨 |
| `--keyexpr=` | `**` | Zenoh subscription key expression |
| `--port=` | `8080` | HTTP 서버 포트 |

## Live Topics

Zenoh mode에서 구독하는 ROS topic. Depth topic은 구독하지 않는다.

| Topic | Type | 용도 |
| --- | --- | --- |
| `/camera/color/image_raw/compressed` | `sensor_msgs/msg/CompressedImage` | RGB viewer |
| `/utlidar/robot_odom` | `nav_msgs/msg/Odometry` | Trajectory |
| `print` | `std_msgs/msg/String` | Stdout panel |

## API

| Endpoint | 설명 |
| --- | --- |
| `GET /` | 웹 UI |
| `GET /api/topics` | 현재 source topic 목록 |
| `GET /api/viewer/frames` | frame metadata, revision, pointing 상태 |
| `GET /api/viewer/image?stream=rgb&index=0&rev=N` | Viewer image. Zenoh mode는 RGB만 제공 |
| `POST /api/live/instruction` | text instruction을 `192.168.0.90:5000/query`로 forward |
| `POST /api/live/pointing` | red dot image goal payload를 `192.168.0.90:5000/query`로 forward |
| `WS /ws` | `viewer_update` 이벤트 |

Pointing 동작:

- UI preview는 이미지 위 DOM overlay로 표시한다.
- `/api/live/pointing` payload의 이미지는 red dot이 픽셀에 합성된 JPEG다.
- Pointing mode에서 trajectory waypoint를 클릭하면 해당 odom timestamp가 포함된 자연어 instruction을 `/api/live/instruction`으로 보낸다.
- pointing 이후 upstream은 RGB frame publish를 계속해야 한다.
- `/api/viewer/frames`의 `rgb_stale_after_pointing=true`는 pointing 후 새 RGB frame이 들어오지 않았다는 뜻이다.

## Debug

```bash
ros2 run --prefix 'gdb -ex run --args' \
  go2_monitor_cpp monitor_server --source=zenoh
```
