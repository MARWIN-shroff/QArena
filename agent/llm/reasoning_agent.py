# agent/llm/reasoning_agent.py

from agent.llm.llm_client import LLMClient
from agent.llm.prompts import FAILURE_ANALYSIS_PROMPT


class ReasoningAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def analyze_failure(self, test_output: str, failure_type: str) -> dict:
        prompt = FAILURE_ANALYSIS_PROMPT.format(
            test_output=test_output,
            failure_type=failure_type
        )

        llm_response = self.llm.generate(prompt)

        return {
            "llm_explanation": llm_response,
            "confidence": "MEDIUM",
            "source": "LLM_REASONING"
        }
