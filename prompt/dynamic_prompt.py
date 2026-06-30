from langchain_openai import ChatOpenAi
import streamlit as st
from dotenv import load_env

load_env()

model = ChatOpenAi()

paper_input = st.selectbox("select the reserach paper",["attention is all you need","BERT","GPT-3","DIFFISUION MODEL BEATS gans"])
style_input = st.selectbox("select he explation style",["beignner-friendly","technical","code-oriented","mathmetical"])
length_input = st.selectbox('select explation length',["in 100 words","in 200 words","in 300 words"])


if st.button("summeries"):
    result =model.invoke(user_input)
    st.write(result.content)