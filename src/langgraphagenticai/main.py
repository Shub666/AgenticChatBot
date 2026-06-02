import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.llms.groqllm import GroqLLM 
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraphagenticai_app():
    """
    Loads the LangGraphAgenticAI Streamlit application, allowing users to select LLMs, use cases, and input necessary credentials.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error("Failed to load user input from UI")
        return
    user_message=st.chat_input("Enter your message here...")

    if user_message:
        try:
            obj_llm_config =GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model.")
                return
            
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("No use case selected. Please select a use case to proceed.")
                return
            
            graph_builder= GraphBuilder(model=model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase=usecase, graph=graph,user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up the graph for the use case '{usecase}': {str(e)}")
                return
            

        except Exception as e:
            st.error(f"Error initializing the LLM model: {str(e)}")
            return