from flask import Flask, jsonify
import os

app = Flask(__name__)

# Designer-Adressen aus Umgebungsvariablen
DESIGNERS = [
    {"name": "Michi", "address": os.getenv("DESIGNER_1")},
    {"name": "Pek", "address": os.getenv("DESIGNER_2")},
    {"name": "Sebi", "address": os.getenv("DESIGNER_3")},
    {"name": "Mike", "address": os.getenv("DESIGNER_4")},
    {"name": "Laura", "address": os.getenv("DESIGNER_5")},
    {"name": "Stephan", "address": os.getenv("DESIGNER_6")}
]

@app.route("/designers", methods=["GET"])
def get_designers():
    return jsonify(DESIGNERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
