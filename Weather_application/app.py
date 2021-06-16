from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.sqlite3'

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form["city"]

        if name:
            cities = City(name)
            db.session.add(cities)
            db.session.commit()

    cities = City.query.order_by(City.id.desc()).all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        weather = {
            'city': city.name,
            'country': r['sys']['country'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('index_weather.html', weather_data=weather_data)

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
