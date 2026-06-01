import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_current_weather(lat: float, lon: float, units: str = "metric", lang: str = "es") -> dict | None:
    """
    Obtiene el clima actual usando coordenadas geográficas.

    Args:
        lat: Latitud de la ciudad
        lon: Longitud de la ciudad
        units: 'metric', 'imperial' o 'standard'
        lang: Código de idioma (ej: 'es', 'en')

    Returns:
        dict con los datos del clima o None si hay error
    """
    params = {
        "lat": lat,       # ✅ coordenadas en lugar de "q"
        "lon": lon,
        "appid": API_KEY,
        "units": units,
        "lang": lang
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            print(f"❌ Error: {data.get('message', 'Error desconocido')}")
            return None

        return data
    except requests.exceptions.Timeout:
        return {"error": "⏰ La solicitud ha excedido el tiempo de espera"}
    except requests.exceptions.ConnectionError:
        return {"error": "🔌 Error de conexión. Verifica tu conexión a internet"}
    except requests.exceptions.RequestException as e:
        return {"error": f"❌ Error en la solicitud: {e}"}
    except ValueError as e:
        return {"error": f"❌ Error al procesar JSON: {e}"}

def get_weather_description(data : dict) -> dict:
    return {
        "ciudad":           data["name"],
        "pais":             data["sys"]["country"],
        "temperatura":      round(data["main"]["temp"]),
        "sensacion":        round(data["main"]["feels_like"]),
        "descripcion":      data["weather"][0]["description"],
        "humedad":          data["main"]["humidity"],
        "icono":            data["weather"][0]["icon"],
        "error":            None
    }

if __name__ == "__main__":
    resultado = get_current_weather( 19.0717, -97.0461) #cordenadas de coscomatepec
    print(resultado)