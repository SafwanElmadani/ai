from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# from vector import retriever


model = OllamaLLM(model="llama3.1")

template = """
You will be helping to answer questions about msp430 mcu!
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

result = chain.invoke({})

print(result)
