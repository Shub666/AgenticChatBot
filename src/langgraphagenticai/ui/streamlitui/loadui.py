import streamlit as st
import os
from src.langgraphagenticai.ui.uniconfig import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(),layout='wide')
        st.header(self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            ## LLMselection
            self.user_controls['selected_llm'] = st.selectbox('Select LLM', llm_options)

            if self.user_controls['selected_llm'] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_model'] = st.selectbox('Select Groq Model', model_options)
                self.user_controls['groq_api_key']= st.session_state['groq_api_key'] = st.text_input('Enter Groq API Key', type='password')

                if not self.user_controls['groq_api_key']:
                    st.warning("Please enter your Groq API Key to proceed. Don't have one? Get it from https://console.groq.com/keys")
       
            ## Use case selection

            self.user_controls["selected_usecase"] = st.selectbox('Select Use Cases', usecase_options)

            if self.user_controls["selected_usecase"] == "ChatBot with WebTool":
               os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state['TAVILY_API_KEY'] = st.text_input("Enter Tavily API Key   ", type="password")

               if not self.user_controls["TAVILY_API_KEY"]:
                   st.warning("Please enter your Tavily API Key to proceed. Don't have one? Get it from https://app.tavily.com/")

        return self.user_controls