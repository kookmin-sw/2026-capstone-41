#include "go2_monitor_cpp/monitor_runner.hpp"

#include <string>

namespace {

std::string get_arg(int argc, char** argv, const std::string& prefix, const std::string& default_value) {
  for (int i = 1; i < argc; ++i) {
    const std::string arg(argv[i]);
    if (arg.rfind(prefix, 0) == 0) {
      return arg.substr(prefix.size());
    }
  }
  return default_value;
}

}  // namespace

int main(int argc, char** argv) {
  go2_monitor_cpp::MonitorRunnerOptions options;
  options.source = get_arg(argc, argv, "--source=", "zenoh");
  options.endpoint = get_arg(argc, argv, "--endpoint=", "udp/127.0.0.1:7447");
  options.keyexpr = get_arg(argc, argv, "--keyexpr=", "**");
  options.port = static_cast<std::uint16_t>(std::stoi(get_arg(argc, argv, "--port=", "8080")));
  return go2_monitor_cpp::run_monitor_server(options);
}
