import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_unsplash_images(estado):
    url_base = "https://api.unsplash.com/search/photos"
    access_key = os.getenv("UNSPLASH_ACCESS_KEY") 
    
    parametros = {
        "query": f"{estado}",
        "orientation": "landscape",
        "per_page": 6 # Traemos 6 opciones por si quieres mostrar una galería
    }
    
    headers = {
        "Authorization": f"Client-ID {access_key}"
    }
    
    try:
        response = requests.get(url_base, params=parametros, headers=headers)
        response.raise_for_status()
        datos = response.json()
        return datos
    except Exception as e:
        return {"error": str(e), "fotos": []}
    
def get_image_description(datos: dict) -> dict:
    fotos_procesadas = []
    for foto in datos.get("results", []):
        # Creamos un diccionario simplificado por cada foto
        info_foto = {
            "id": foto["id"],
            "descripcion": foto["description"] or foto["alt_description"] or "Sin descripción",
            "url_regular": foto["urls"]["regular"],
            "url_small": foto["urls"]["small"],
            "autor": {
                "nombre": foto["user"]["name"],
                "perfil": foto["user"]["links"]["html"]
            }
        }
        fotos_procesadas.append(info_foto)
    
    return {
        "fotos": fotos_procesadas,
        "error": None
    }
    
if __name__ == "__main__":
    print(get_unsplash_images("Veracruz"))