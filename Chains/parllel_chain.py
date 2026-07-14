from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from lngchain_core.output_parser import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableParallel


load_dotenv()


mmodel1 = ChatOpenAI()
model2 = chatanthropic()

prompt1 = PromptTemplate(
    template="generate a 5 facts about the given topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a 5 pointer summary about text: {text}",
    input_variables=["text"]
)


prompt3 = PromptTemplate(
    template="merge the facts and summary into single document :{topic}and{text} ",
    input_variables=["topic","text"]
)

parser = StrOutputParser()

Parllel_chain = RunnableParallel({
    
    "facts": prompt1 | model1 | parser,
    "summary": prompt2 | model2 | parser,
    "merged": prompt3 | model1 | parser

})

merged_chain =  prompt3 | model1 | parser

chain = Parllel_chain | merged_chain

result = chain.invoke({"topic": "Python programming"})

print(result) 

