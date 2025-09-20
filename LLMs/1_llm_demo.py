from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/horizon-beta",   
)

response = llm.invoke("What is the capital of India?")
print("LLM Response:", response.content)
