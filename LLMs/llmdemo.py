from langchain_openai import OpenAI 
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9)
result = llm.invoke("Write a tagline for an ice cream shop.")    
print(result)
b 