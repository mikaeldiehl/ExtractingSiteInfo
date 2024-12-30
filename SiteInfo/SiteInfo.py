import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

loader = WebBaseLoader('https://asimov.academy/')
lista_documentos = loader.load()
print(lista_documentos)

documento = ''
for doc in lista_documentos:
  documento = documento + doc.page_content
  print(documento)

print(lista_documentos[0].page_content)

api_key = ''
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado Asimo e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}'),
    ('user', '{input}')
])

chain = template | chat
resposta = chain.invoke({'documentos_informados': documento, 'input': 'Quais as trilhas disponíveis na Asimov?'})

print(resposta.content)