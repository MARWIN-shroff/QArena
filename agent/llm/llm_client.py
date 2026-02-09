# agent/llm/llm_client.py

class LLMClient:
    def __init__(self, model_name: str = "mock"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        """
        Single responsibility:
        Takes prompt → returns raw LLM text
        """
        if self.model_name == "mock":
            return self._mock_response(prompt)

        raise NotImplementedError("Real LLM not plugged yet")

    def _mock_response(self, prompt: str) -> str:
        return (
            "The failure appears to be caused by a mismatch "
            "between expected and actual outputs. "
            "This likely indicates a logic bug in the tested function."
        )
