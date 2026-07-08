from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    MessagesPlaceholder(variable_name="history"),
    ('human', "Explain in simple terms, what is {topic}?")
])

chat_history = []
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create a prompt with the chat history

prompt = chat_template.invoke( {'history': chat_history, 'query': "What is the difference between supervised and unsupervised learning?, and where is my refund?"} )