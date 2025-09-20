from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

# Load environment variables (.env should have HUGGINGFACEHUB_API_TOKEN)
load_dotenv()

# Initialize LLaMA 3 model from Hugging Face
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",  # You can change to 70B version if needed
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.header('Research Tool')

# Dropdown for paper selection
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Dropdown for explanation style
style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

# Dropdown for explanation length
length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load prompt template from file (template.json must exist in same dir)
template = load_prompt('template.json')

# Button to run summarization
if st.button('Summarize'):
    chain = template | model
    with st.spinner("Generating explanation..."):
        result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        st.write(result.content)
