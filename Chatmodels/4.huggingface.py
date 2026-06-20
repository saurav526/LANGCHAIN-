from langchain_huggingface import ChatHuggingFaceHub , HUggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = HuggingFaceEndpoint(
repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
task = "Text Generation" 
)
model = ChatHuggingFaceHub(llm=llm)

result = model.invoke("Write a tagline for MS Dhoni.")
print(result.content)
