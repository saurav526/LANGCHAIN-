from langchain_OpenAI import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model= ChatOpenAI()

chat_history = []

while True:
    user_input = input("User: ")
    chat_history.append(("user", user_input))
    if user_input.lower() == "exit":
        break

    prompt = f"User: {user_input}\nAI:"
    response = model.invoke(chat_history)
    chat_history.append(("ai", response.content))
    print(f"AI: {response.content}")

print(chat_history)