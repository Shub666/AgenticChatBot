import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input


    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input['groq_api_key']
            selected_groq_model=self.user_controls_input['selected_model']
            if groq_api_key =="" and os.getenv("GROQ_API_KEY") == "":
                st.error("Groq API Key is required. Please enter it in the sidebar.")

            llm=ChatGroq(model=selected_groq_model, api_key=groq_api_key) # type: ignore
        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {str(e)}")
        return llm