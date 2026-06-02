from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import json
import streamlit as st


class DisplayResultStreamlit:
    def __init__(self,usecase, graph,user_message):
        self.graph = graph
        self.usecase = usecase
        self.user_message = user_message


    def display_result_on_ui(self):
        usecse = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecse == "Basic ChatBot":
            for event in graph.stream({'messages':("user",user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)
                        