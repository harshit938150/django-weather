import urllib.request
import json
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=10de42a2cf9836f76724ed31ca9861c9').read()
        jdata = json.loads(source)

        data = {
            "temp": str(jdata['main']['temp']) + ' °C',
            "humidity": str(jdata['main']['humidity']),
            'main': str(jdata['weather'][0]['main']),
            'description': str(jdata['weather'][0]['description']),
            'icon': jdata['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)