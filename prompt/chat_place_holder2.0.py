from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "{query}")
])

history = [
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a programming language.")
]

prompt = chat_template.format_prompt(
    domain="AI",
    chat_history=history,
    query="What are its main uses?"
)

print(prompt.to_messages())