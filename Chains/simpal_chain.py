from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from lngchain_core.output_parser import StrOutputParser


load_dotenv()

prompt = PromptTemplate(
    template="generate a 5 facts about the given topic: {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "Python programming"})

print(result)

chain.get_graph().print_ascii()

