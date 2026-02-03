from typing import Dict


def analyze_results(stdout: str, stderr: str) -> Dict[str, str]:
    """
    Analyzes pytest output and classifies failures
    with root-cause hints.
    """

    combined_output = (stdout + "\n" + stderr).lower()

    # ---------- PASS ----------
    if "failed" not in combined_output and "error" not in combined_output:
        return {
            "status": "PASS",
            "classification": "All tests passed",
            "root_cause": "No issues detected",
            "suggestion": "No action required"
        }

    # ---------- FAILURE CLASSIFICATION ----------
    if "importerror" in combined_output or "modulenotfounderror" in combined_output:
        return {
            "status": "FAIL",
            "classification": "Import Error",
            "root_cause": "Project modules are not being resolved correctly",
            "suggestion": "Check PYTHONPATH or module imports"
        }

    if "assertionerror" in combined_output:
        return {
            "status": "FAIL",
            "classification": "Assertion Failure",
            "root_cause": "Business logic does not match expected behavior",
            "suggestion": "Review function logic or expected outputs"
        }

    if "typeerror" in combined_output:
        return {
            "status": "FAIL",
            "classification": "Type Error",
            "root_cause": "Incorrect function arguments or return type",
            "suggestion": "Verify function signature and test inputs"
        }

    if "nameerror" in combined_output:
        return {
            "status": "FAIL",
            "classification": "Name Error",
            "root_cause": "Referenced variable or function does not exist",
            "suggestion": "Check spelling and scope of identifiers"
        }

    if "syntaxerror" in combined_output:
        return {
            "status": "FAIL",
            "classification": "Syntax Error",
            "root_cause": "Invalid Python syntax detected",
            "suggestion": "Fix syntax issues before running tests"
        }

    if "collectionerror" in combined_output:
        return {
            "status": "FAIL",
            "classification": "Test Collection Error",
            "root_cause": "Pytest failed to collect test files",
            "suggestion": "Ensure test files and imports are valid"
        }

    # ---------- FALLBACK ----------
    return {
        "status": "FAIL",
        "classification": "Unknown Error",
        "root_cause": "Unrecognized failure pattern",
        "suggestion": "Inspect pytest logs for more details"
    }
