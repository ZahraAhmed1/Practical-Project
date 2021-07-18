from os import getenv
from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy import desc
from sqlalchemy.sql.expression import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)




class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    winner = db.Column(db.String(50), nullable=False)




@app.route('/')
def home():
    
    animal= requests.get('http://A_animal_api:5000/get_animal')
    country = requests.get('http://A_country_api:5000/get_country')
    winner=requests.post('http://A_winner_api:5000/get_winner',json={'animal':animal.text , 'country':animal.text})
    
    last_five_duels = Animals.query.order_by(desc(Animals.id)).limit(5).all()
    db.session.add(
        Animals(
            type = animal.text,
            country = country.text,
            winner = winner.text
        )
    )
    db.session.commit()

    return render_template('home.html',animal=animal.text,country=country.text,winner=winner.text,last_five_duels=last_five_duels)
    

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True) 