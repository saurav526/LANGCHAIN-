from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file  
documents = [
    "delhi is the captail of india"
    "kolkata is the captail of west bengal"
    "patana is the is the captail of bihar"
    "paris  is the captail of france"
]
result = embedding.embed_documents(documents) 

print(str(result ))
