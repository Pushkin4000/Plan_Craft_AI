import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq
llm=ChatGroq(model="openai/gpt-oss-120b",temperature=0.6)

from langchain.agents import AgentType, initialize_agent,load_tools

tool=load_tools(['ddg-search'],llm=llm)

agent=initialize_agent(
    tool,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# missing agent.run command