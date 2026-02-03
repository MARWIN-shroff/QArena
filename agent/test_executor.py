import subprocess

def execute_tests():
    result = subprocess.run(
        ["pytest", "-q"],
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr
