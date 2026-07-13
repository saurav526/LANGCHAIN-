from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.invoke({"topic": "The impact of climate change on global agriculture."})

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})

result2 = model.invoke(prompt2)

print(result2.content)