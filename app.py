from flask import Flask

import service.service

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to this Page!'


@app.route('/load')
def load():
    return service.service.load()


@app.route('/weather')
def weather():
    return service.service.get_weather()


@app.route('/weather/<city_name>')
def city_weather(city_name):
    return service.service.get_city_weather(city_name)


if __name__ == '__main__':
    app.run()
