from langchain_google_genai import ChatGoogleGenerativeAI   
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
chat_model = ChatGoogleGenerativeAI(model="gpt-3.5-turbo", temperature=0.9)
result = chat_model.invoke("Write a tagline for an ice cream shop.")

print(result.content)