from django.shortcuts import render
from datetime import datetime
from threading import Timer
import requests
import json
import threading

# Create your views here.
def index(request):

    api_address = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Atlanta%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

    #JSON

    json_data = requests.get(api_address).json()

    temperature = json_data['query']['results']['channel']['item']['condition']['temp']
    description = json_data['query']['results']['channel']['item']['condition']['text']
    date = json_data['query']['results']['channel']['item']['condition']['date']
    forecast = json_data['query']['results']['channel']['item']['forecast'][0]['high']

    print(description)

    #Emoji dictionary

    emojiList = {
        'Mostly Cloudy': ':cloud:',
        'Sunny': ':sunny:' ,
        'Cloudy': ':cloud:',
        'Mostly Sunny': ':mostly_sunny:',
        'Partly Cloudy': ':partly_sunny:',
        'Breezy': ':wind_blowing_face:',
        'Heavy Rain': ':rain_cloud:',
        'Rain': ':rain_cloud:'
    }


    emoji = ''

    for k, v in emojiList.items():
        if k == description:
            emoji = v

    weatherUpdate = 'The temperature is ' + temperature + ' degrees F and ' + description + emoji + ' in Atlanta.' + '\n The high today is ' + forecast + '.'
    # print statement

    weatherForecast = {
        'forecast': weatherUpdate
    }

    print(weatherForecast)
    
    return render(request,'WeatherApi/index.html',context=weatherForecast)
