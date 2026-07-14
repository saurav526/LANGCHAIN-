from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from lngchain_core.output_parser import StrOutputParser


load_dotenv()

prompt1 = PromptTemplate(
    template="generate a 5 facts about the given topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a 5 pointer summary about text: {text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Python programming"})
print(result)
