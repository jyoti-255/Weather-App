
from django.shortcuts import render, HttpResponse
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mumbai'
    
    url = f"https://api.weatherapi.com/v1/current.json?key=af865a2b65fc4875b42182428240407&q={city}"
    response = requests.get(url)
    data = response.json()

    description = data['current']['condition']['text']
    icon = data['current']['condition']['icon'].split('/')[-1].split('.')[0]
    temp = data['current']['temp_c']
    day = datetime.date.today()
    
    return render(request, "home.html", {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day
    })



