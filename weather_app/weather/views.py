# weather/views.py
import requests
from django.shortcuts import render

def index(request):
    # Paste your OpenWeatherMap API key here
    API_KEY = '3008332ca625079be34e3ffacd799f70'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    weather_data = None
    error_msg = None

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        
        if city:
            # Make the API call
            response = requests.get(url.format(city, API_KEY)).json()
            
            # Check if OpenWeatherMap successfully found the city
            if response.get('cod') == 200:
                weather_data = {
                    'city': response['name'],
                    'country': response['sys']['country'],
                    'temperature': round(response['main']['temp']),
                    'description': response['weather'][0]['description'].capitalize(),
                    'icon': response['weather'][0]['icon'],
                    'humidity': response['main']['humidity'],
                    'wind_speed': response['wind']['speed'],
                }
            else:
                error_msg = "City not found! Please check the spelling and try again."
        else:
            error_msg = "Please enter a city name."

    context = {
        'weather_data': weather_data,
        'error_msg': error_msg
    }
    
    return render(request, 'weather/index.html', context)