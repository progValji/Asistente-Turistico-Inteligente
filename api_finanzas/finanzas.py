import requests

BASE_URL = "https://mx.dolarapi.com/v1/cotizaciones"
MONEDA = "usd"

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
        "compra":   data["compra"],
        "error":    None
    }

if __name__ == "__main__":
    resultado = get_stock_price()
    print(resultado)