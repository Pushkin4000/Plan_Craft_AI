from langchain_ollama import ChatOllama

llm=ChatOllama(model="hf.co/unsloth/Qwen2.5-Omni-3B-GGUF:Q2_K_XL")

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

Poxs=PromptTemplate(
    input_variable=["Technology"],
    template="Reply with only one word answer: Tell me a project name regarding {Technology}."
)

proj_chain= LLMChain(llm=llm,prompt=Poxs,output_key="project_name")


Poxs2=PromptTemplate(
    input_variable=["project_name","Technology"],
    template="Generate me steps in detailed numerical order to perform this technology {Technology} with project name being this {project_name}"
)

proj_full=LLMChain(llm=llm,prompt=Poxs2,output_key="Procedure")

from langchain.chains import SequentialChain

chain = SequentialChain(
    chains =[proj_chain,proj_full],
    input_variables=["Technology"],
    output_variables=["project_name","Procedure"]
)        

def techo(Technology):
    return chain(Technology)
