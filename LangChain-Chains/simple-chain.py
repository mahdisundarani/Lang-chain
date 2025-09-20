from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from grandalf.graphs import Edge, Graph, Vertex 

from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="list 3 facts about {topic}",
    input_variables=["topic"]   
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "cat"})

print(result)

chain.get_graph().print_ascii()  # to visualize the chain
