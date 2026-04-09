from flask import Flask, render_template, request
from integrador.integrador import obtener_info_turistica

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    ciudad_input = ""

    if request.method == "POST":
        ciudad_input = request.form.get("estados", "").strip()
        if ciudad_input:
            resultado = obtener_info_turistica(ciudad_input)

    return render_template("index.html", resultado=resultado, ciudad_input=ciudad_input)

if __name__ == "__main__":
    app.run(debug=True)