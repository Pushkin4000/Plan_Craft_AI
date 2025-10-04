import os 
import time
import agent_works

os.environ['GROQ_API_KEY']=("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")

from langchain_groq import ChatGroq
llm=ChatGroq(model="deepseek-r1-distill-llama-70b",temperature=0.6,reasoning_format="hidden")

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
    

