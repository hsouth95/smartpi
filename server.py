from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    description = 'No weather data'
    with open('/tmp/weather.json', 'r') as weather_file:
        data = json.load(weather_file)
        description = data['weather'][0]['description']

    return description
