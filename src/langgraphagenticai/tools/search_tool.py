from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Define and return a list of tools for the chatbot.
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Create and return a ToolNode for the chatbot.
    This function initializes a ToolNode with the provided tools, allowing the chatbot to utilize these tools in its interactions.
    """
    tool_node=ToolNode(tools=tools)
    return tool_node