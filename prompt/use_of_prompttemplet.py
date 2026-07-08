from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Create model
model = ChatOpenAI()

# Streamlit UI
paper_input = st.selectbox(
    "Select the research paper",
    [
        "Attention Is All You Need",
        "BERT",
        "GPT-3",
        "Diffusion Models Beat GANs"
    ]
)

style_input = st.selectbox(
    "Select the explanation style",
    [
        "Beginner-friendly",
        "Technical",
        "Code-oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select explanation length",
    [
        "100 words",
        "200 words",
        "300 words"
    ]
)

# Prompt Template
template = load_prompt_template("prompt_template.json") 
#assuming you have saved the template in a JSON file named "prompt_template.json" in the same directory.

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,})
st.write(result.content)