from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_winner', methods=['POST'])
def get_winner():
    winner {
        
    }

if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True )