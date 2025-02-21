from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import re

model=OllamaLLM(model='deepseek-r1')
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Empty Response:** If no information matches the description, return an empty string ('')."
    "2. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "3. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "4. **Exclude <think> Sections:** Any text enclosed within `<think> ... </think>` must not appear in the output."
    "5. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)


def extract_with_deepseek(dom_cunks,parse_description):
    promt=ChatPromptTemplate.from_template(template=template)
    chain=promt | model
    parse_result=[]
    for i,chunk in enumerate(dom_cunks,start=1):
        response=chain.invoke({
            'dom_content':chunk,'parse_description':parse_description
        })
        parse_result.append(response)
    return '\n'.join(parse_result)

