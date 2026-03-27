import os
import requests
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import tool

# --- 1. Definición de Herramienta ---
@tool
def obtener_datos_gatos(count: int = 1) -> str:
    """
    Obtiene uno o varios datos curiosos sobre los gatos.
    Args:
        count: El número de datos curiosos que el usuario quiere obtener.
    """
    url = f"https://meowfacts.herokuapp.com/?count={count}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return str(datos["data"])
        return "No pude obtener datos ahora mismo."
    except Exception as e:
        return f"Error de conexión: {e}"

tools = [obtener_datos_gatos]

# --- 2. Configuración ---
os.environ["OPENAI_API_KEY"] = "tu-api-key-aqui" # <--- ¡CAMBIA ESTO!

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- 3. Inicialización del Agente (Versión más compatible) ---
agent_executor = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.OPENAI_FUNCTIONS, # O usa STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
    verbose=True
)

# --- 4. Ejecución ---
if __name__ == "__main__":
    pregunta = "¿Me puedes dar 3 datos curiosos de los gatos?"
    print(f"\nPregunta: {pregunta}")
    
    # En versiones antiguas se usa .run(), en modernas .invoke()
    try:
        resultado = agent_executor.invoke({"input": pregunta})
        print("\nRespuesta Final:", resultado["output"])
    except AttributeError:
        resultado = agent_executor.run(pregunta)
        print("\nRespuesta Final:", resultado)