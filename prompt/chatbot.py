from langchain_OpenAI import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model= ChatOpenAI()

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    prompt = f"User: {user_input}\nAI:"
    response = model.invoke(prompt)
    print(f"AI: {response.content}")