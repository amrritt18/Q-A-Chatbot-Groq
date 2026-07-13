import streamlit as st
import groq
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

#Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with GROQ"

#prompt templet

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "You are a helpful assistant. Please response to user queries"),
        ('user','Question:{question}')
    ]
)

def generate_response(question, api_key, model_name, temperature, max_tokens):
    llm = ChatGroq(
        groq_api_key=api_key,
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain.invoke({"question": question})

## Title of the app
st.title('Enhance Q&A Chatbot with GROQ')
api_key = st.sidebar.text_input('Enter your Groq API key:', type = 'password')

## Drop down to select various Groq AI model
llm = st.sidebar.selectbox('Select a Groq AI Model:',['llama-3.3-70b-versatile','llama-3.1-8b-instant','meta-llama/llama-4-scout-17b-16e-instruct'])

#Adjust response parameter
temperature = st.sidebar.slider('Temperature',min_value=0.0,max_value=1.0,value=0.7)
max_token = st.sidebar.slider('Max Tokens',min_value=50,max_value=300,value=150)

#Main interface for user input
st.write('Go ahead and ask any question')
user_input = st.text_input('You:')
if user_input:
    if not api_key:
        st.warning("Please enter your Groq API key.")
    else:
        response = generate_response(
            user_input,
            api_key,
            llm,
            temperature,
            max_token
        )
        st.write(response)