from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

from dotenv import load_dotenv

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

Merge_chain = prompt3 | model1 | parser

chain = parallel_chain | Merge_chain

text = """ 
                       
A black hole is an astronomical body so dense that its gravity prevents anything from escaping, even light. Albert Einstein's theory of general relativity predicts that a sufficiently compact mass will form a black hole.[4] The boundary of no escape is called the event horizon. In general relativity, a black hole's event horizon seals an object's fate but produces no locally detectable change when crossed.[5] In many ways, a black hole acts like an ideal black body, as it reflects no light.[6][7] Quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional to its mass. This temperature is of the order of billionths of a kelvin for stellar black holes, making it essentially impossible to observe directly.

"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()  # to visualize the chain