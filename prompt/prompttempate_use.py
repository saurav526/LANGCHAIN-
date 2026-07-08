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
template = PromptTemplate(
    template="""
Summarize the research paper "{paper_input}" in the following style:

Explanation Style: {style_input}
Explanation Length: {length_input}

Also include:
1. Mathematical details.
2. Relevant equations (if applicable).
3. Intuitive explanations of the mathematics.
4. Simple code examples where appropriate.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

# Create prompt
prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    }
)

# Button
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)