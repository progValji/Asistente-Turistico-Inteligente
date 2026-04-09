from api_clima.clima import get_current_weather, get_weather_description
from api_finanzas.finanzas import get_stock_price, get_stock_price_description
from api_imagenes.imagenes import get_unsplash_images, get_image_description


def obtener_info_turistica(ciudad: str) -> dict:
    """
    Integra los datos de clima, finanzas e imágenes para una ciudad.

    Args:
        ciudad: Nombre de la ciudad (ej: "Puebla,MX")

    Returns:
        dict con toda la información turística consolidada
    """

    # ─── 1. Llamar a cada servicio de forma independiente ───────────────────
    clima    = get_current_weather(ciudad)
    finanzas = get_stock_price()
    imagenes = get_unsplash_images(ciudad)

    # ---- Datos ya filtrados----
    clima_datos_filtrados = get_weather_description(clima)
    finanzas_datos_filtrados = get_stock_price_description(finanzas)
    imagenes_datos_filtrados = get_image_description(imagenes)

    # ─── 2. Detectar errores por servicio ────────────────────────────────────
    errores = {}

    if clima_datos_filtrados.get("error"):
        errores["clima"] = clima["error"]

    if finanzas_datos_filtrados.get("error"):
        errores["finanzas"] = finanzas["error"]

    if imagenes_datos_filtrados.get("error"):
        errores["imagenes"] = imagenes["error"]

    # ─── 3. Consolidar y retornar ─────────────────────────────────────────────
    return {
        "ciudad":   ciudad,
        "clima":    clima_datos_filtrados,
        "finanzas": finanzas_datos_filtrados,
        "imagenes": imagenes_datos_filtrados.get("fotos", []),
        "errores":  errores,          # dict vacío {} si todo salió bien
        "exito":    len(errores) == 0  # True solo si los 3 servicios funcionaron
    }
