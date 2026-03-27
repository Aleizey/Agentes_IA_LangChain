from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage
from langchain.tools import tool, ToolRuntime
from dataclasses import dataclass

modelo = ChatOllama(model="llama3.2:latest")

TIENDAS = [
    {"nombre": "Zara", "age": 70},
    {"nombre": "Pull&Bear", "age": 150}
    ]

@dataclass
class ContenxtClass():
    LISTA_PERSONAJES: list[dict] # Valor estatico

@tool
def Meridiano_Nuevo(contexto: ToolRuntime[ContenxtClass]):
    """ 
    Funcion para optener las tiendas de ropa que hay en españa
    """

    personaje_runtime = contexto.context.LISTA_PERSONAJES

    return personaje_runtime

modelo = ChatOllama(model="llama3.2:latest")
agente = create_agent(model=modelo, tools=[Meridiano_Nuevo], context_schema=ContenxtClass)

mensaje = [
    SystemMessage(content="Eres un IA capas de responder preguntas que te haga sin problema"),
    HumanMessage(content="Dime una tienda en España con mas de 100 años"),
]

respuesta = agente.invoke(input={"messages": mensaje}, context=ContenxtClass(LISTA_PERSONAJES=[TIENDAS]) )
print(respuesta["messages"][-1].content)       