import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = "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"

#Langsmith Tracking
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
os.environ['LANGSMITH_TRACING'] = "true"
os.environ['LANGSMITH_API_KEY'] = "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"
os.environ["LANGSMITH_PROJECT"]="Q&A Chatbot with GROQ"
## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please reponse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key="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")
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
llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key="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")


if user_input:
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please ask your question")
