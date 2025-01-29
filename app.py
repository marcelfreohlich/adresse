from flask import Flask, jsonify
import os

app = Flask(__name__)

# Designer-Adressen aus Umgebungsvariablen
DESIGNERS = [
    {"name": "Michi", "Josef Musser-Straße 11, 2514, Wienersdorf": os.getenv("DESIGNER_1")},
    {"name": "Pek", "Keutschach 41, 9074, Keutschach": os.getenv("DESIGNER_2")},
    {"name": "Sebi", "Unteraumühlweg 6a, 5400, Hallein": os.getenv("DESIGNER_3")},
    {"name": "Mike", "Lisa Scholl Weg 4, 6170, Zirl": os.getenv("DESIGNER_4")},
    {"name": "Laura", "Seeweg 16, 6212, Maurach": os.getenv("DESIGNER_5")},
    {"name": "Stephan", "Hernsteiner Straße 42 Haus 8, 2551, Enzesfeld-Lindabrunn": os.getenv("DESIGNER_6")}
]

@app.route("/designers", methods=["GET"])
def get_designers():
    return jsonify(DESIGNERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
