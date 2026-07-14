from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal

# Load environment variables
load_dotenv()

# Model
model = ChatOpenAI()

# Output parser
parser = StrOutputParser()

# Pydantic schema
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback"
    )

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Classification prompt
prompt1 = PromptTemplate(
    template="""
    Classify the sentiment of the following feedback as positive or negative.

    Feedback: {feedback}

    {format_instructions}
    """,
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser2.get_format_instructions()
    }
)

# Positive response
prompt2 = PromptTemplate(
    template="Generate a thank you note for the following positive feedback: {feedback}",
    input_variables=["feedback"]
)

# Negative response
prompt3 = PromptTemplate(
    template="Generate an apology note for the following negative feedback: {feedback}",
    input_variables=["feedback"]
)

# Fallback prompt
prompt4 = PromptTemplate(
    template="Please provide a suitable response for: {feedback}",
    input_variables=["feedback"]
)

# Step 1: Classify sentiment
classifier_chain = prompt1 | model | parser2

# Step 2: Branch based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    prompt4 | model | parser
)

# Final chain
chain = classifier_chain | branch_chain

# Run
result = chain.invoke({"feedback": "I hate this product"})
print(result)