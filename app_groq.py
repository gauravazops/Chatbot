import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


import os
from dotenv import load_dotenv
load_dotenv()

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please reponse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,temperature,max_tokens):
    llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)
    output_parser=StrOutputParser()
    chain = prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## Title of the App
st.title("Enhanced Q&A Chatbot with GROQ")

## Adjust reponse params
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

## Main interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")


if user_input:
    response=generate_response(user_input,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please ask your question")
