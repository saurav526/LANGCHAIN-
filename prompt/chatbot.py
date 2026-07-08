from langchain_OpenAI import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage, AIMessage ,SystemMessage


load_dotenv()
model= ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi, how are you?"),
    AIMessage(content="I'm good, thanks! How can I help you today?")
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break

    prompt = f"User: {user_input}\nAI:"
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"AI: {response.content}")

print(chat_history)