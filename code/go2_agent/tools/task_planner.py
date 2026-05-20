import re
from typing import List

from langchain.agents import tool

from llm import get_llm


SYSTEM_PROMPT = """\
You are a task planner for a quadruped robot (Unitree Go2).
Your job is to decompose a complex, long-horizon robot instruction into a sequence of simple, atomic subtasks.

Rules:
1. Number each subtask as "Task 1:", "Task 2:", etc.
2. Each subtask must describe exactly one action step.
3. A subtask may be:
   - a navigation command toward one target object or location, or
   - a single direct motion command with one duration, distance, or angle.
   - just chat with user or explain something.
4. Maintain the original logical order.
5. Output ONLY the numbered task list. No extra explanation.
"""

USER_PROMPT_TEMPLATE = """\
Decompose the following instruction into subtasks.

Instruction: "{instruction}"
"""

_planner_llm = None


def get_planner_llm():
    global _planner_llm

    if _planner_llm is None:
        _planner_llm = get_llm(streaming=False)
    return _planner_llm


def parse_subtasks(response: str) -> List[str]:
    matches = re.findall(r"Task\s+\d+\s*[:\.]\s*(.+)", response, re.MULTILINE)
    return [instruction.strip() for instruction in matches if instruction.strip()]


def decompose_instruction(llm, instruction: str) -> List[str]:
    response = llm.invoke(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": USER_PROMPT_TEMPLATE.format(instruction=instruction),
            },
        ]
    )
    content = getattr(response, "content", response)
    if isinstance(content, list):
        content = "".join(
            part.get("text", "") for part in content if isinstance(part, dict)
        )
    subtasks = parse_subtasks(str(content).strip())
    return subtasks or [instruction]


def format_subtasks(subtasks: List[str]) -> str:
    return "\n".join(
        "Task %s: %s" % (index + 1, subtask)
        for index, subtask in enumerate(subtasks)
    )


@tool
def task_planner(instruction: str) -> str:
    # """
    # Break a complex long-horizon or multi-step Go2 robot instruction into atomic subtasks.
    # Use this before executing requests that contain multiple ordered goals, locations, or actions.
    # Do not use this for simple one-step movement, stop/status requests, or ordinary conversation.
    # After this returns, execute the numbered tasks one at a time in order.
    # """
    """
    Break any multi-step Go2 robot instruction into atomic subtasks.
	Use this before executing any request that contains more than one ordered action, goal, or location, even if the request is short or simple.
	Examples that require this tool: "go 1m and turn right 90 degrees", "move forward then sit", "go to the door and turn around".
	Do not use this for single-action movement, stop/status requests, or ordinary conversation.
	After this returns, execute the numbered tasks one at a time in order.
    """
    try:
        subtasks = decompose_instruction(get_planner_llm(), instruction)
    except Exception:
        subtasks = [instruction]
    return format_subtasks(subtasks)
