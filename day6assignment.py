from fastapi import FastAPI, Request
from pydantic import BaseModel
import random
import json
from dicttoxml import dicttoxml
from fastapi.responses import JSONResponse, Response

app = FastAPI()

def generate_weather_data(city: str):
    return {
        "city": city,
        "temperature": random.randint(-10, 40),
        "description": "Clear sky" if random.random() > 0.5 else "Cloudy",
        "humidity": random.randint(30, 90),
        "wind_speed": random.randint(1, 20)
    }

@app.get("/weather/{city}")
async def get_weather(city: str, format: str = "json"):
    weather_data = generate_weather_data(city)
    
    if format.lower() == "xml":
        
        xml_data = dicttoxml(weather_data, custom_root="weather", ids=False)
        return Response(content=xml_data, media_type="application/xml")
    return JSONResponse(content=weather_data)

