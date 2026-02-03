def analyze_results(output: str, error: str):
    if "failed" in output.lower():
        return "❌ Tests failed. Possible logic error."
    return "✅ All tests passed."
