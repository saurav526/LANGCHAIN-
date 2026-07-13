from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from unittest import result
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlM/TinyLlama-2-7B-GGUF",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str 
    age: int
    occupation: str


parser = PydanticOutputParser(pydantic_object=Person)
# we can also use the peompt template to generate the prompt for the model. The prompt template can be used to generate the prompt for the model, and the output parser can be used to parse the output of the model into a pydantic object.
prompt = f"""
Extract the following information.

{parser.get_format_instructions()}

Text:
Alice is a 28-year-old Data Scientist at Microsoft.
"""

response = llm.invoke(prompt)
result = model.invoke(prompt)
print(result)

person = parser.parse(response)

print(person.model_dump())