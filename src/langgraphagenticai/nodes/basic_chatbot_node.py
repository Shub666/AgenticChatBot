

from src.langgraphagenticai.state.state import State


class BasicChatBotNode:
    """
    basic chatbot login implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state:State) -> dict:
        """
        Run the chatbot node with the given input.
        This method processes the input using the language model (LLM) and generates a response. The response is then returned as output.
        """
        
        return {"messages":self.llm.invoke(state["messages"])}