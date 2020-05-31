import requests
from django.shortcuts import render
import os
from os import path

if path.exists("env.py"):
    import env

# Create your views here.
def weather(request):
    if request.method == "POST":
        city = request.POST.get('city')
    else:
        city = 'rotherham'

    google_maps_api_key = os.environ.get('google_maps_api_key')

    weather_api_key = os.environ.get('weather_api_key')
    weather_api = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    

    r = requests.get(weather_api.format(city, weather_api_key)).json()

    try:
        city_weather = {
            'city': city,
            'temperture': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }    
    except:
        city_weather = {
            'error': 'This city does not exist!'
        }

    context = {'city_weather': city_weather, 'google_maps_api_key': google_maps_api_key}

    return render(request, 'weather.html', context)