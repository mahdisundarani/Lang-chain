# app.py

import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="QnA Chat App", layout="centered")

# Initialize the model only once
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        task="text-generation",
    )
    return ChatHuggingFace(llm=llm)

model = load_model()

# UI
st.title("🧠 Ask Anything - QnA Chat with LLaMA 3")

query = st.text_input("Ask a question:")
if st.button("Submit"):
    if query.strip() != "":
        with st.spinner("Thinking..."):
            result = model.invoke(query)
            st.markdown("### Answer:")
            st.success(result.content)
    else:
        st.warning("Please enter a question.")
