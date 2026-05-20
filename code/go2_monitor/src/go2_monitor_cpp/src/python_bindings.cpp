#include "go2_monitor_cpp/monitor_runner.hpp"

#include <pybind11/pybind11.h>

#include <memory>
#include <mutex>

namespace py = pybind11;

namespace {

std::mutex active_runner_mutex;
std::shared_ptr<go2_monitor_cpp::MonitorRunner> active_runner;

go2_monitor_cpp::MonitorRunnerOptions make_options(
  const std::string& source,
  const std::string& endpoint,
  const std::string& keyexpr,
  std::uint16_t port) {
  go2_monitor_cpp::MonitorRunnerOptions options;
  options.source = source;
  options.endpoint = endpoint;
  options.keyexpr = keyexpr;
  options.port = port;
  return options;
}

std::shared_ptr<go2_monitor_cpp::MonitorRunner> replace_active_runner(
  const go2_monitor_cpp::MonitorRunnerOptions& options) {
  std::shared_ptr<go2_monitor_cpp::MonitorRunner> previous_runner;
  {
    std::lock_guard<std::mutex> lock(active_runner_mutex);
    previous_runner = std::move(active_runner);
  }

  if (previous_runner) {
    previous_runner->stop();
    previous_runner->join();
  }

  auto runner = go2_monitor_cpp::start_monitor_background(options);
  {
    std::lock_guard<std::mutex> lock(active_runner_mutex);
    active_runner = runner;
  }
  return runner;
}

void stop_active_runner() {
  std::shared_ptr<go2_monitor_cpp::MonitorRunner> runner;
  {
    std::lock_guard<std::mutex> lock(active_runner_mutex);
    runner = std::move(active_runner);
  }

  if (runner) {
    runner->stop();
    runner->join();
  }
}

}  // namespace

PYBIND11_MODULE(go2_monitor, m) {
  m.doc() = "Python bindings for go2_monitor_cpp";

  py::class_<go2_monitor_cpp::MonitorRunnerOptions>(m, "monitor_option")
    .def(py::init<>())
    .def_readwrite("source", &go2_monitor_cpp::MonitorRunnerOptions::source)
    .def_readwrite("endpoint", &go2_monitor_cpp::MonitorRunnerOptions::endpoint)
    .def_readwrite("keyexpr", &go2_monitor_cpp::MonitorRunnerOptions::keyexpr)
    .def_readwrite("port", &go2_monitor_cpp::MonitorRunnerOptions::port);

  py::class_<go2_monitor_cpp::MonitorRunner, std::shared_ptr<go2_monitor_cpp::MonitorRunner>>(
    m, "monitor_runner")
    .def("stop", &go2_monitor_cpp::MonitorRunner::stop, py::call_guard<py::gil_scoped_release>())
    .def("join", &go2_monitor_cpp::MonitorRunner::join, py::call_guard<py::gil_scoped_release>())
    .def("is_running", &go2_monitor_cpp::MonitorRunner::is_running);

  m.def(
    "start_monitor",
    [](const go2_monitor_cpp::MonitorRunnerOptions& options) {
      return replace_active_runner(options);
    },
    py::arg("options") = go2_monitor_cpp::MonitorRunnerOptions{});

  m.def(
    "start_monitor",
    [](const std::string& source,
       const std::string& endpoint,
       const std::string& keyexpr,
       std::uint16_t port) {
      return replace_active_runner(make_options(source, endpoint, keyexpr, port));
    },
    py::arg("source") = "zenoh",
    py::arg("endpoint") = "udp/127.0.0.1:7447",
    py::arg("keyexpr") = "**",
    py::arg("port") = 8080);

  m.def(
    "run_monitor",
    [](const go2_monitor_cpp::MonitorRunnerOptions& options) {
      return go2_monitor_cpp::run_monitor_server(options);
    },
    py::arg("options") = go2_monitor_cpp::MonitorRunnerOptions{},
    py::call_guard<py::gil_scoped_release>());

  m.def(
    "run_monitor",
    [](const std::string& source,
       const std::string& endpoint,
       const std::string& keyexpr,
       std::uint16_t port) {
      return go2_monitor_cpp::run_monitor_server(make_options(source, endpoint, keyexpr, port));
    },
    py::arg("source") = "zenoh",
    py::arg("endpoint") = "udp/127.0.0.1:7447",
    py::arg("keyexpr") = "**",
    py::arg("port") = 8080,
    py::call_guard<py::gil_scoped_release>());

  m.def("stop_monitor", &stop_active_runner, py::call_guard<py::gil_scoped_release>());

  m.attr("MonitorOption") = m.attr("monitor_option");
  m.attr("MonitorRunnerOptions") = m.attr("monitor_option");
  m.attr("MonitorRunner") = m.attr("monitor_runner");
  m.attr("run_monitor_server") = m.attr("run_monitor");
}
