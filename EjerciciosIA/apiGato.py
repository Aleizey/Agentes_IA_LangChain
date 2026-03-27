import requests
from langchain_core.tools import tool

@tool
def obtener_dato_gato() -> str:
    """Obtiene un único dato curioso y aleatorio sobre los gatos."""
    url = "https://meowfacts.herokuapp.com/"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos["data"][0]
    else:
        return "Lo siento, la API de gatos no está disponible en este momento."
    
@tool
def obtener_varios_datos_gatos(count: int = 1) -> list:
    """
    Obtiene uno o varios datos curiosos sobre los gatos.
    Args:
        count: El número de datos curiosos que el usuario quiere obtener. Por defecto es 1.
    """
    url = f"https://meowfacts.herokuapp.com/?count={count}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos["data"]
    else:
        return ["Lo siento, no pude contactar con el servidor felino."]

tools = [obtener_varios_datos_gatos]

datos = obtener_varios_datos_gatos.func(count=2) 
print(datos)

