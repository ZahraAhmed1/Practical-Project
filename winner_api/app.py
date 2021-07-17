from flask import Flask, request 
import random

app = Flask(__name__)

@app.route("/get_winner",methods=["POST"])
def get_winner():
    animal=request.get_json()
    country=request.get_json()

    if len(animal["animal"]) >= len(country["country"]):
        winner="win"
    else:
        winner="lose"
    return winner
      

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    