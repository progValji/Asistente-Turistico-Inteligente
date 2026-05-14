from api_clima.clima import get_current_weather, get_weather_description
from api_finanzas.finanzas import get_stock_price, get_stock_price_description
from api_imagenes.imagenes import get_unsplash_images, get_image_description

def obtener_info_turistica(ciudad: str, lat: float, lon: float) -> dict:
    """
    Integra los datos de clima, finanzas e imágenes para una ciudad.

    Args:
        ciudad: Nombre de la ciudad (solo para Unsplash y para mostrar en UI)
        lat: Latitud de la ciudad
        lon: Longitud de la ciudad
    """

    # ─── 1. Llamar a cada servicio ───────────────────────────────────────────
    clima    = get_current_weather(lat, lon)   # ✅ coordenadas
    finanzas = get_stock_price()
    imagenes = get_unsplash_images(ciudad)     # ✅ nombre (Unsplash no usa coords)

    # ─── 2. Filtrar datos ────────────────────────────────────────────────────
    clima_datos_filtrados    = get_weather_description(clima)
    finanzas_datos_filtrados = get_stock_price_description(finanzas)
    imagenes_datos_filtrados = get_image_description(imagenes)

    # ─── 3. Detectar errores ─────────────────────────────────────────────────
    errores = {}

    if clima_datos_filtrados.get("error"):
        errores["clima"] = clima_datos_filtrados["error"]   # ✅ era clima["error"], bug corregido

    if finanzas_datos_filtrados.get("error"):
        errores["finanzas"] = finanzas_datos_filtrados["error"]

    if imagenes_datos_filtrados.get("error"):
        errores["imagenes"] = imagenes_datos_filtrados["error"]

    # ─── 4. Consolidar y retornar ─────────────────────────────────────────────
    return {
        "ciudad":   ciudad,
        "clima":    clima_datos_filtrados,
        "finanzas": finanzas_datos_filtrados,
        "imagenes": imagenes_datos_filtrados.get("fotos", []),
        "errores":  errores,
        "exito":    len(errores) == 0
    }
