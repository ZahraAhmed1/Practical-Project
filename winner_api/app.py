from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_winner',methods=(['GET']))
def get_winner():
    winner=random.choice(['winning and saved their mum.','losing and so the other animals ate their mum'])
    return winner    
      

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    