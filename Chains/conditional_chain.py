from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from lngchain_core.output_parser import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.schema.runnable import RunnableParallel,RunnableBranch ,RunnableLamda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from itertools import chain



load_dotenv()


model1 = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the follllowing text into positvie and negative: {feedback}\n {fromat_instruction}",
    input_variables=["feedback"],
    partial_variables={"fromate_instruction":parser2.get_format_instructions()}

)

prompt2 = PromptTemplate(
    template="generate a thank you note for the following positive feedback: {feedback}",
    input_variables=["feedback"]

)

prompt3 = PromptTemplate(
    template="generate a thank you note for the following NEGATIVE feedback: {feedback}",
    input_variables=["feedback"]

)
prompt4 = PromptTemplate(
    template="pls select/choose the appropriate reason:{reason}",
    input_variables=["reason"]
)

classifier_chain = prompt1 | model1 | parser2

branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", prompt2 | model1 | parser),
    (lambda x: x["sentiment"] == "negative", prompt3 | model1 | parser),
    prompt4 | model1 | parser
)

chain_final = classifier_chain | branch_chain
result = chain.invoke({"feedback": "I hate this product"})
print(result)