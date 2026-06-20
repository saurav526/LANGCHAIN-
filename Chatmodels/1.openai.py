from lanchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

result = chat_model.invoke("what is the capital of USA?")

print(result.content)   