import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Sidebar contents
with st.sidebar:
    st.title('LLM Chat app')
    st.markdown('''
                ## About
                This app is an llm-powered chatbot built using:
                - [streamlit](https://streamlit.com/)
                - [Langchain](https://python.langchain.com/)
                - [OpenAI](https://platform.openai.com/docs/models) LLM model
                ''')
    add_vertical_space(5)
    st.write('First streamlit')