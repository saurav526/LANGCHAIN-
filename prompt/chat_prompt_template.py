from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "Explain in simple terms, what is {topic}?")
])

prompt = chat_template.format_prompt(domain="AI", topic="machine learning")
print(prompt.to_messages())