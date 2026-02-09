# agent/llm/prompts.py

FAILURE_ANALYSIS_PROMPT = """
You are a senior software test engineer.

Given:
- Test execution output
- Failure classification
- Project structure

Explain:
1. What likely went wrong
2. Where the issue may exist
3. What the developer should check first

Be concise and technical.

Test Output:
{test_output}

Failure Type:
{failure_type}
"""
