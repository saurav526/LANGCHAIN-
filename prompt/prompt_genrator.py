from lagchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Summarize the research paper "{paper_input}" in the following style:

Explanation Style: {style_input}
Explanation Length: {length_input}

Also include:
1. Mathematical details.
2. Relevant equations (if applicable).
3. Intuitive explanations of the mathematics.
4. Simple code examples where appropriate.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)
template.save("prompt_template.json")
