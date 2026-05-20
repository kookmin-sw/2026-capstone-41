cmake_minimum_required(VERSION 3.16)
project(go2_monitor_cpp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(GO2_MONITOR_BUILD_BENCHMARK "Build viewer benchmark server" OFF)
option(
  GO2_MONITOR_BUILD_PYTHON_DEPLOYMENT
  "Build a relocatable Python deployment bundle under lib/${PROJECT_NAME}/python_deploy"
  OFF
)
set(
  GO2_MONITOR_PYTHON_DEPLOY_DIR
  "lib/${PROJECT_NAME}/python_deploy"
  CACHE STRING
  "Install directory for the relocatable Python deployment bundle"
)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(SQLite3 REQUIRED)
find_package(JPEG REQUIRED)
find_package(PNG REQUIRED)

list(APPEND CMAKE_PREFIX_PATH "$ENV{HOME}/.local")

execute_process(
  COMMAND "${Python3_EXECUTABLE}" -m pybind11 --cmakedir
  OUTPUT_VARIABLE pybind11_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(pybind11 CONFIG REQUIRED)

find_package(zenohc REQUIRED)
find_package(zenohcxx REQUIRED)

include(FetchContent)
FetchContent_Declare(
  crow
  GIT_REPOSITORY https://github.com/CrowCpp/Crow.git
  GIT_TAG v1.2.1
)
FetchContent_MakeAvailable(crow)

ament_get_python_install_dir(PYTHON_INSTALL_DIR)
_ament_cmake_python_register_environment_hook()

get_filename_component(GO2_MONITOR_ROS_PREFIX "${rclcpp_DIR}/../../.." ABSOLUTE)
set(GO2_MONITOR_ROS_LIB_DIR "${GO2_MONITOR_ROS_PREFIX}/lib")
set(GO2_MONITOR_LOCAL_LIB_DIR "$ENV{HOME}/.local/lib")
set(GO2_MONITOR_COMMON_RPATH
  "${GO2_MONITOR_LOCAL_LIB_DIR};${GO2_MONITOR_ROS_LIB_DIR}"
)
set(GO2_MONITOR_PYTHON_INSTALL_RPATH "${GO2_MONITOR_COMMON_RPATH}")
if(GO2_MONITOR_BUILD_PYTHON_DEPLOYMENT)
  list(PREPEND GO2_MONITOR_PYTHON_INSTALL_RPATH "\$ORIGIN")
endif()

add_library(go2_monitor_core
  src/log_db_reader.cpp
  src/monitor_runner.cpp
  src/viewer_data_source.cpp
  src/web_server.cpp
  src/zenoh_monitor.cpp
)
set_target_properties(go2_monitor_core PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_include_directories(go2_monitor_core PUBLIC
  include
)

ament_target_dependencies(go2_monitor_core
  nav_msgs
  rclcpp
  sensor_msgs
  std_msgs
)

target_link_libraries(go2_monitor_core
  SQLite::SQLite3
  JPEG::JPEG
  PNG::PNG
  zenohcxx::zenohc
  Crow::Crow
)

add_executable(monitor_server
  src/main.cpp
)
set_target_properties(monitor_server PROPERTIES
  BUILD_RPATH "${GO2_MONITOR_COMMON_RPATH}"
  INSTALL_RPATH "${GO2_MONITOR_COMMON_RPATH}"
)

target_link_libraries(monitor_server
  go2_monitor_core
)

pybind11_add_module(go2_monitor MODULE
  src/python_bindings.cpp
)
if(GO2_MONITOR_BUILD_PYTHON_DEPLOYMENT)
  target_link_options(go2_monitor BEFORE PRIVATE "LINKER:--no-as-needed")
endif()
set_target_properties(go2_monitor PROPERTIES
  BUILD_RPATH "${GO2_MONITOR_COMMON_RPATH}"
  INSTALL_RPATH "${GO2_MONITOR_PYTHON_INSTALL_RPATH}"
)

target_link_libraries(go2_monitor PRIVATE
  go2_monitor_core
)

if(GO2_MONITOR_BUILD_BENCHMARK)
  add_executable(viewer_benchmark_server
    ../../benchmarks/viewer_revision/benchmark_server.cpp
    src/viewer_data_source.cpp
    src/web_server.cpp
  )

  ament_target_dependencies(viewer_benchmark_server
    rclcpp
    sensor_msgs
  )

  target_include_directories(viewer_benchmark_server PRIVATE
    include
  )

  target_link_libraries(viewer_benchmark_server
    JPEG::JPEG
    PNG::PNG
    Crow::Crow
  )

  install(TARGETS
    viewer_benchmark_server
    DESTINATION lib/${PROJECT_NAME}
  )
endif()

install(TARGETS
  go2_monitor_core
  monitor_server
  DESTINATION lib/${PROJECT_NAME}
)

install(TARGETS
  go2_monitor
  LIBRARY DESTINATION ${PYTHON_INSTALL_DIR}
)

if(GO2_MONITOR_BUILD_PYTHON_DEPLOYMENT)
  configure_file(
    cmake/install_python_deployment.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/install_python_deployment.cmake
    @ONLY
  )

  install(TARGETS
    go2_monitor
    LIBRARY DESTINATION ${GO2_MONITOR_PYTHON_DEPLOY_DIR}
  )

  install(SCRIPT ${CMAKE_CURRENT_BINARY_DIR}/install_python_deployment.cmake)
endif()

ament_package()
