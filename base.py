class BaseAgent:
    def process(self, text: str) -> dict:
        raise NotImplementedError
