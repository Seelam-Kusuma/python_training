from flask import Flask, request, jsonify
import random
import json
from dicttoxml import dicttoxml

app = Flask(__name__)

def generate_weather_data(city):
    return {
        "city": city,
        "temperature": random.randint(-10, 40),  
        "description": "Clear sky" if random.random() > 0.5 else "Cloudy",
        "humidity": random.randint(30, 90),
        "wind_speed": random.randint(1, 20)
    }

]
@app.route('/weather/<city>', methods=['GET'])
def weather(city):
    format_type = request.args.get('format', 'json').lower()
    weather_data = generate_weather_data(city)
    if format_type == 'xml':
        return dicttoxml(weather_data, custom_root='weather', ids=False)
 
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
