from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_animal', methods=['GET'])
def get_animal():
    return random.choice(['whale', 'fox', 'lizard', 'cat', 'dog', 'ox'])

if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True )