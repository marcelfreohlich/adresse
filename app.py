from flask import Flask, jsonify
import os

app = Flask(__name__)

# Aktiviere CORS für alle Routen
CORS(app, origins="https://marcelfreohlich.github.io/Entfernung/")

# Designer-Adressen aus Umgebungsvariablen
DESIGNERS = [
    {"name": "Michi", "address": os.getenv("DESIGNER_1", "Josef Musser-Straße 11, 2514, Wienersdorf")},
    {"name": "Pek", "address": os.getenv("DESIGNER_2", "Keutschach 41, 9074, Keutschach")},
    {"name": "Sebi", "address": os.getenv("DESIGNER_3", "Unteraumühlweg 6a, 5400, Hallein")},
    {"name": "Mike", "address": os.getenv("DESIGNER_4", "Lisa Scholl Weg 4, 6170, Zirl")},
    {"name": "Laura", "address": os.getenv("DESIGNER_5", "Seeweg 16, 6212, Maurach")},
    {"name": "Stephan", "address": os.getenv("DESIGNER_6", "Hernsteiner Straße 42 Haus 8, 2551, Enzesfeld-Lindabrunn")}
]

@app.route("/designers", methods=["GET"])
def get_designers():
    return jsonify(DESIGNERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
