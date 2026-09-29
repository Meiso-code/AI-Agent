class Agent:
    def __init__(self, name: str, model: str = "gpt-4o-mini"):
        self.name = name
        self.model = model

    def run(self, message: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def think(self, message: str) -> str:
        return f"Thinking about: {message}"