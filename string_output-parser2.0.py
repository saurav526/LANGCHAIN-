from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchian_core.output_parsers import StringOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlM/TinyLlama-2-7B-GGUF",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="write a summary of the following text:/n {topic}",
    input_variables=["topic"]
)


template2 = PromptTemplate(
    template="write a quiz or 5 question on the topic of the following text:/n {text}",
    input_variables=["text"]
)

parser = StringOutputParser()

chain = template1 | model | parser | template2 | model | parser


result = chain.invoke({"topic": "The impact of climate change on global agriculture."})

print(result)