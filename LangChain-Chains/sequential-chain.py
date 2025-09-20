from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from grandalf.graphs import Edge, Graph, Vertex

from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="give detailed report about {topic}",
    input_variables=["topic"]
)

promnpt2 = PromptTemplate(
    template="make a brief summary of the {topic}",  
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

# chain = prompt1 | model | parser 

# result1 = chain.invoke({"topic": "Black holes"})

# print("Detailed Report: \n",result1)

# chain = promnpt2 | model | parser

# result2 = chain.invoke({"topic": result1})

# print("Summary: \n",result2)

# made a single long chain :
chain = prompt1 | model | parser | promnpt2 | model | parser

result = chain.invoke({"topic": "Black holes"})

print("Final Summary: \n",result)

chain.get_graph().print_ascii()  # to visualize the chain

