from langchain_openai import ChatOpenAi
import streamlit as st
from dotenv import load_env
from lanchain_core.prompts import PromptTemplate    

load_env()

model = ChatOpenAi()

paper_input = st.selectbox("select the reserach paper",["attention is all you need","BERT","GPT-3","DIFFISUION MODEL BEATS gans"])
style_input = st.selectbox("select he explation style",["beignner-friendly","technical","code-oriented","mathmetical"])
length_input = st.selectbox('select explation length',["in 100 words","in 200 words","in 300 words"])

template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template="summarize the research paper {paper_input} in a " \
    "explation style: {style_input}  and" \
    "explation length: {length_input}" \
    "1. Mathmetical detail:" \
    "-include the relevent mathmetical equations and derivations" \
    "explain the mathmetical concepts using simple ,intutive code}"
    "" \
)

prompt= template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input

})

if st.button("summeries"):
    result =model.invoke(prompt)
    st.write(result.content)