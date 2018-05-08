from django.shortcuts import render
from datetime import datetime
from threading import Timer
import requests
import json
import threading
import random
import array

# Create your views here.
def index(request):

    api_address = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Atlanta%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

    # JSON

    json_data = requests.get(api_address).json()

    temperatureNow = json_data['query']['results']['channel']['item']['condition']['temp']
    descriptionToday = json_data['query']['results']['channel']['item']['condition']['text']
    date = json_data['query']['results']['channel']['item']['condition']['date']
    highToday = json_data['query']['results']['channel']['item']['forecast'][0]['high']
    highTomorrow = json_data['query']['results']['channel']['item']['forecast'][1]['high']
    descriptionTomorrow = json_data['query']['results']['channel']['item']['forecast'][1]['text']

   # print(forecastTomorrow)
    print(descriptionToday)

    # Emoji dictionary

    backgroundList = {}

    backgroundList.setdefault('Mostly Sunny', []).append('clearsky.jpg')
    backgroundList.setdefault('Mostly Sunny', []).append('lightning.gif')
    backgroundList.setdefault('Partly Cloudy', []).append('rain2.gif')
    backgroundList.setdefault('Partly Cloudy', []).append('CRg.gif')
    backgroundList.setdefault('Mostly Cloudy', []).append('natureback.jpg')
    backgroundList.setdefault('Mostly Cloudy', []).append('rain.jpg')
    backgroundList.setdefault('Sunny', []).append('sunny1.gif')
    backgroundList.setdefault('Sunny', []).append('lightning.gif')
    backgroundList.setdefault('Breezy', []).append('windy.jpg')
    backgroundList.setdefault('Heavy Rain', []).append('heavyrain.jpg')
    backgroundList.setdefault('Heavy Rain', []).append('rain.jpg')
    backgroundList.setdefault('Rain', []).append('rainy1.jpg')
    backgroundList.setdefault('Rain', []).append('rain.jpg')
    backgroundList.setdefault('Cloudy', []).append('CRg.gif')
    backgroundList.setdefault('Cloudy', []).append('cloudy2.jpg')

    backgroundImg = ''


    for k, v in backgroundList.items():
        if k == descriptionToday:
            backgroundImg = random.choice(v)


    # print statement

    weatherUpdate = 'The temperature is ' + temperatureNow + ' degrees F and ' + descriptionToday + ' in Atlanta.' + '\n The high today is ' + highToday + '. \n Tomorrow : ' + highTomorrow + " and " + descriptionTomorrow


    weatherForecast = {
        'forecast': weatherUpdate,
        'temperature': temperatureNow,
        'background': backgroundImg,
    }

    print(weatherForecast)

    return render(request,'WeatherApi/index.html',context=weatherForecast)
