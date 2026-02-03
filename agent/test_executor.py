import subprocess
import os
from typing import Tuple


def execute_tests(project_path: str) -> Tuple[str, str]:
    """
    Executes pytest in a project-aware manner by injecting
    the project path into PYTHONPATH.
    """

    if not os.path.exists(project_path):
        raise ValueError("Invalid project path")

    env = os.environ.copy()
    env["PYTHONPATH"] = project_path

    process = subprocess.run(
        ["pytest", "tests", "-q"],
        capture_output=True,
        text=True,
        env=env
    )

    return process.stdout, process.stderr
