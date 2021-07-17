from flask import Flask, jsonify,request
import random

app = Flask(__name__)

@app.route("/get_animal",methods=["GET"])
def get_animal():
    animals=random.choice(["bear","fish","cat","tiger"])
    return animals

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)