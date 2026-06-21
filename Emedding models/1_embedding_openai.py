from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file  

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimension=400)
result = embeddings.embed_query("What is Artificial Intelligence?") 
print(str(result   ))
