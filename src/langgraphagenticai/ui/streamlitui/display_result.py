from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
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
        elif usecse == "ChatBot with WebTool":
            initial_state={"messages":[user_message]}
            res=graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call end")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)   
        
        elif usecse == "AI News":
            frequency= self.user_message
            with st.spinner("Fetching ans summarizing news..."):
                result=graph.invoke({"messages":frequency})
                try:
                    AI_NEWS_PATH=f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content= file.read()

                    st.markdown(markdown_content,unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News not generated or file not found:{AI_NEWS_PATH}") # type: ignore
                except Exception as e:
                    st.error(f"An error occured: {str(e)}")

                        