from langchain_openai import  ChatOpenAi
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAi()
st.header("Research tool")

user_input = st.text_input("enter your text")

if st.button("summeries"):
   result = model.invoke(user_input)

   st.write(result.content)
