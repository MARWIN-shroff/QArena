import os
import ast
from typing import List


EXCLUDED_DIRS = {"tests", "__pycache__", ".venv", "venv"}


def _get_python_files(project_path: str) -> List[str]:
    python_files = []

    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            if file.endswith(".py") and not file.startswith("test_"):
                python_files.append(os.path.join(root, file))

    return python_files


def _extract_functions(file_path: str) -> List[str]:
    functions = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except Exception:
        return functions

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions


def generate_tests(project_path: str) -> List[str]:
    """
    Generates pytest-style test stubs for discovered Python functions
    and writes them into the tests/ directory.
    """
    if not os.path.exists(project_path):
        raise ValueError("Invalid project path")

    os.makedirs("tests", exist_ok=True)

    generated_tests = []
    python_files = _get_python_files(project_path)

    for file_path in python_files:
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        functions = _extract_functions(file_path)

        if not functions:
            continue

        test_file_path = os.path.join("tests", f"test_{module_name}.py")

        with open(test_file_path, "w", encoding="utf-8") as test_file:
            test_file.write(f"import pytest\n")
            test_file.write(f"from {module_name} import *\n\n")

            for func in functions:
                test_code = f"""
def test_{func}():
    \"\"\"Auto-generated test for {func}\"\"\"
    result = {func}()
    assert result is not None
"""
                test_file.write(test_code)
                generated_tests.append(test_code.strip())

    return generated_tests

