from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a frictional character {formatted_instructions}',
    input_variables=[],
    partial_variables={'formatted_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({})
# model_result = model.invoke(prompt)
# result = parser.parse(model_result.content)
# these three lines can be replaced by a chain:
chain = template | model | parser
result = chain.invoke({})

print(result)
print(type(result))
print('Name: ',result['name'])
