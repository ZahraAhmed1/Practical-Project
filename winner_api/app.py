from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_winner',methods=(['GET']))
def get_winner():
    winner=random.choice(['win','lose'])
    return winner    
      

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    