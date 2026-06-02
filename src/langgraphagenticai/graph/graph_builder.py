from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBotNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the 'BasicChatBotNode' class
        and intigrate it into the graph. The chatbot node is set as both exit and entry point of the graph, allowing for a simple conversational flow.
        """

        self.basic_chatbot_node=BasicChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self,usecase):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic ChatBot":
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()