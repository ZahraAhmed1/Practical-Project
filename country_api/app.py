from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/get_country',methods=["POST"])
def get_country():
    country = {
        "bear":"yemen",
        "cat": "japan",
        "fish":"jamaica",
        "tiger":"france"

    }
    return country[request.data.decode('utf-8')] 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True )