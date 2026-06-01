import requests
from datetime import datetime

BASE_URL = "https://mx.dolarapi.com/v1/cotizaciones"
MONEDA = "usd"

def get_current_date_formatted() -> str:
    ahora = datetime.now()
    periodo = "a.m" if ahora.hour < 12 else "p.m"
    hora_12 = ahora.hour if ahora.hour <= 12 else ahora.hour - 12
    if hora_12 == 0:
        hora_12 = 12
    
    return f"{ahora.day}/{ahora.month}/{ahora.year}, {hora_12}:{ahora.minute:02d}:{ahora.second:02d} {periodo}"
    
def get_stock_price():
    try:
        url = f"{BASE_URL}/{MONEDA}"

        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()
        return datos
    except requests.exceptions.RequestException as e:
        return {"error": f"❌ Error en la solicitud: {e}"}
    
def get_stock_price_description(data: dict) -> dict:
    return {
        "moneda":   data["moneda"],
        "nombre":   data["nombre"],
        "compra":   round(data["compra"], 2),
        "fecha": get_current_date_formatted(),
        "error":    None
    }

if __name__ == "__main__":
    resultado = get_stock_price()
    print(resultado)