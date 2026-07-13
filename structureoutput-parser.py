from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructureOutputParser,ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlM/TinyLlama-2-7B-GGUF",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="name", description="the name of the fictional person"),
    ResponseSchema(name="age", description="the age of the fictional person"),
    ResponseSchema(name="gender", description="the gender of the fictional person"),
    ResponseSchema(name="city", description="the city of the fictional person")
]

parser = StructureOutputParser.from_response_schemas(schema=schema)

template1 = PromptTemplate(
    template ="give me a name ,age ,gender  and city of a fictional person {topic} \n {fromat_instructions}",
    input_variables=["topic"],
    partial_variables={"fromat_instructions": parser.get_format_instructions()}
)   
# can also use the chain to combine the prompt template, model, and output parser into a single callable object. This allows you to easily generate a prompt, invoke the model, and parse the output in one step.
prompt = template1.invoke({"topic": "a fantasy character from a medieval world"})
print(prompt)

model_result = model.invoke(prompt)
final_result = parser.parse(model_result.content)
print(final_result)
