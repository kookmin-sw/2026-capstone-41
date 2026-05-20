import os
import subprocess
import termios
import threading
import requests

from langchain.agents import tool
from .ros2 import execute_ros_command


THREAD_STATE_TOPIC = "/thread_state"
TOGGLE_THREAD_SERVICE = "/toggle_run_threads"
SET_BOOL_SERVICE_TYPE = "std_srvs/srv/SetBool"
THREAD_STATE_TIMEOUT = 3.0
_vln_cancel = threading.Event()


def _save_terminal_state():
    try:
        tty_fd = os.open("/dev/tty", os.O_RDWR)
        tty_state = termios.tcgetattr(tty_fd)
        return tty_fd, tty_state
    except OSError:
        return None, None


def _restore_terminal_state(tty_fd, tty_state):
    if tty_fd is None or tty_state is None:
        return
    try:
        termios.tcsetattr(tty_fd, termios.TCSADRAIN, tty_state)
    finally:
        os.close(tty_fd)


def _toggle_client_thread(enable):
    request = "{data: true}" if enable else "{data: false}"
    _, output = execute_ros_command(
        f'ros2 service call {TOGGLE_THREAD_SERVICE} {SET_BOOL_SERVICE_TYPE} "{request}"'
    )
    output = output.strip()
    if output:
        return output
    return "Requested client thread on." if enable else "Requested client thread off."


def _check_thread_state_raw() -> str:
    tty_fd, tty_state = _save_terminal_state()
    try:
        with open(os.devnull, "r") as devnull:
            result = subprocess.run(
                ["script", "-q", "-c", f"ros2 topic echo {THREAD_STATE_TOPIC}", "/dev/null"],
                stdin=devnull,
                check=False,
                capture_output=True,
                text=True,
                timeout=THREAD_STATE_TIMEOUT,
            )
            output = f"{result.stdout}\n{result.stderr}"
    except subprocess.TimeoutExpired as exc:
        output = f"{exc.stdout or ''}\n{exc.stderr or ''}"
    finally:
        _restore_terminal_state(tty_fd, tty_state)

    return output.lower()


@tool
def check_client_status() -> str:
    """Check the InternVLN client thread status from /thread_state.
    if status is false you can turn on the client thread to execute the high-level tools for vln server."""
    output = _check_thread_state_raw()
    if "data: true" in output:
        return "Client thread is on."
    if "data: false" in output:
        return "Client thread is off."
    if output.strip():
        return output.strip()
    return "Unable to determine client thread status."


def _wait_for_internvln_success() -> bool:
    started = False
    for _ in range(10):
        if _vln_cancel.is_set():
            return False
        output = _check_thread_state_raw()
        if "data: true" in output:
            started = True
            break

    if not started:
        return False

    while not _vln_cancel.is_set():
        output = _check_thread_state_raw()
        if "data: false" in output:
            return True

    return False


def _set_command(command):
    r = requests.post(
        "http://192.168.0.60:5801/update_instruction",
        data=command,
        timeout=3,
    )
    if r.ok:
        return None
    output = r.text.strip()
    if output:
        return output
    return f"Error: failed to update instruction ({r.status_code})"


@tool
def client_thread_on(command) -> str:
    """Enable the InternVLN client control/planning threads.
    It should process the user's command for vln server.
    you don't need to ask about the permission.
    """
    # but, after you execute it, please check the thread state before executing next command"""
    print(command)
    error = _set_command(command)
    if error:
        return error
    _vln_cancel.clear()
    _toggle_client_thread(True)
    success = _wait_for_internvln_success()
    return "Navigation complete." if success else "Navigation cancelled."


@tool
def client_thread_off() -> str:
    """Disable the InternVLN client control/planning threads.
    you don't need to ask about the permission.
    """
    return _toggle_client_thread(False)
