from flask import Flask, render_template, jsonify,request
import requests, random

app = Flask(__name__)

@app.route('/')
def fight():
    animal = requests.get('http://animal_api:5000/get_animal')
    winner = requests.get('http://winner_api:5000/get_winner')
    country = requests.post('http://country_api:5000/get_country',data=animal.text)

    return render_template('home.html', animal=animal.text, winner=winner.text, country=country.text) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
