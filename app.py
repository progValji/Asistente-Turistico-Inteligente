from flask import Flask, render_template, request, jsonify
from integrador.integrador import obtener_info_turistica
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")

load_dotenv()

RAPID_KEY = os.getenv("RAPIDAPI_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    ciudad_input = ""

    if request.method == "POST":
        ciudad_input = request.form.get("ciudad", "").strip()
        lat = request.form.get("lat")
        lon = request.form.get("lon")
        try:
            lat = float(lat)
            lon = float(lon)
        except(ValueError):
            error = "Selecciona una ciudad de la lista de sugerencias."
        if ciudad_input:
            resultado = obtener_info_turistica(ciudad_input, lat, lon)

    return render_template("index.html", resultado=resultado, ciudad_input=ciudad_input, error=error)

@app.route("/buscar-ciudades")
def buscar_ciudades():
    query = request.args.get("q", "").strip()
    if len(query) < 2:
        return jsonify([])

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    headers = {
        "x-rapidapi-key": RAPID_KEY,
        "x-rapidapi-host": "wft-geo-db.p.rapidapi.com"
    }
    params = {
        "namePrefix": query,
        "countryIds": "MX",       # solo México
        "languageCode": "es",
        "minPopulation": 50000,   # evita pueblitos desconocidos
        "limit": 6,
        "sort": "-population"     # primero las más grandes
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        ciudades = [
            {
                "nombre": city["city"],
                "display": f"{city['city']}, {city['region']}",
                "lat": city["latitude"],
                "lon": city["longitude"],
            }
            for city in data.get("data", [])
        ]
        return jsonify(ciudades)
    except Exception as e:
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)