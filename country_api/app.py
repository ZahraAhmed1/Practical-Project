from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_country', methods=['GET'])
def get_country():
    return random.choice(['peru', 'sudan', 'romania'])


if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True )