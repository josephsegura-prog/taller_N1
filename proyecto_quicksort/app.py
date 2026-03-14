# app.py
# Backend Flask que recibe un archivo txt con personas
# y las ordena alfabéticamente usando QuickSort

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Servidor activo"

# ----------------------------
# QUICK SORT
# ----------------------------

def partition(arr, low, high):
    pivot = arr[high]["nombre"].lower()
    i = low - 1

    for j in range(low, high):
        if arr[j]["nombre"].lower() <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# ----------------------------
# LEER TXT
# ----------------------------

def leer_txt(texto):
    registros = []
    lineas = texto.split("\n")

    for linea in lineas:
        if linea.strip() == "":
            continue

        partes = linea.split(",")

        if len(partes) != 3:
            continue

        nombre = partes[0].strip()
        edad = partes[1].strip()
        ciudad = partes[2].strip()

        try:
            edad = int(edad)
        except:
            pass

        registros.append({
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        })

    return registros


# ----------------------------
# ENDPOINT
# ----------------------------

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "no se envió archivo"}), 400

    archivo = request.files["file"]
    contenido = archivo.read().decode("utf-8")

    datos = leer_txt(contenido)

    if len(datos) > 0:
        quicksort(datos, 0, len(datos)-1)

    return jsonify(datos)


if __name__ == "__main__":
    app.run(debug=True)
