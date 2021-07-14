from flask import Flask, render_template, 
import requests

app = Flask(__name__)

@app.route('/')
def home():
    animal = requests.get('http://duel:5000/get_animal')
    country = requests.get('http://duel:5000/get_country')
    winner = requests.post('http://duel:5000/get_winner')
    return render_template('home.html', animal=animal.text, country=country.text, winner=winner.text )

if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True )
