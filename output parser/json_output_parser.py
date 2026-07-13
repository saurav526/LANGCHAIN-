from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlM/TinyLlama-2-7B-GGUF",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template ="give me a name ,age ,gender and city of a fictional person \n {fromat_instructions}",
    input_variables=[],
    partial_variables={"fromate_instructions": parser.get_format_instructions()}
)
# can also use the chain to combine the prompt template, model, and output parser into a single callable object. This allows you to easily generate a prompt, invoke the model, and parse the output in one step.
# chain = template1 | model | parser

# result2 = chain.invoke({})
# print(result2)

prompt = template1.invoke({})

print(prompt)

result = model.invoke(prompt)

print(result.content)

final_result = parser.parse(result.content)
print(final_result)

print(type(final_result))
