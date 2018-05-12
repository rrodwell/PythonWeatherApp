from django.shortcuts import render
from datetime import datetime
from threading import Timer
import requests
import json
import threading
import random
import array
import datetime
from django.utils import timezone




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

    sunrise = json_data['query']['results']['channel']['astronomy']['sunrise']
    sunset = json_data['query']['results']['channel']['astronomy']['sunset']

    new_sunrise = sunrise.replace("am", "")
    new_sunset = sunset.replace("pm", "")


   # print(forecastTomorrow)
    print(descriptionToday)

    # Emoji dictionary

    now = datetime.datetime.now().time()
    morning_begin = now.replace(hour=6, minute=0, second=0, microsecond=0)
    evening_begin = now.replace(hour=16, minute=21, second=0, microsecond=0)
    night_begin = now.replace(hour=20, minute=0, second=0, microsecond=0)

    backgroundList = {}


    if now > morning_begin and now < evening_begin:

        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or'Sunny' or ' Mostly Sunny':
            backgroundList.setdefault('Partly Cloudy', []).append('clearsky.jpg')
            backgroundList.setdefault('Partly Cloudy', []).append('CRg.gif')
            backgroundList.setdefault('Partly Cloudy', []).append('sunnymorning.gif')
            backgroundList.setdefault('Partly Cloudy', []).append('natureback.jpg')
            backgroundList.setdefault('Cloudy', []).append('clearsky.jpg')
            backgroundList.setdefault('Cloudy', []).append('CRg.gif')
            backgroundList.setdefault('Cloudy', []).append('sunnymorning.gif')
            backgroundList.setdefault('Cloudy', []).append('natureback.jpg')
            backgroundList.setdefault('Mostly Cloudy', ['CRg.gif']).append('clearsky.jpg')
            backgroundList.setdefault('Mostly Cloudy', []).append('CRg.gif')
            backgroundList.setdefault('Mostly Cloudy', []).append('sunnymorning.gif')
            backgroundList.setdefault('Mostly Cloudy', []).append('natureback.jpg')
            backgroundList.setdefault('Sunny', ['CRg.gif']).append('clearsky.jpg')
            backgroundList.setdefault('Sunny', []).append('CRg.gif')
            backgroundList.setdefault('Sunny', []).append('sunnymorning.gif')
            backgroundList.setdefault('Sunny', []).append('natureback.jpg')
            backgroundList.setdefault('Sunny', ['CRg.gif']).append('clearsky.jpg')
            backgroundList.setdefault('Sunny', []).append('CRg.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('sunnymorning.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('natureback.jpg')





    elif now > evening_begin and now < night_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny' or 'Most Sunny':
            backgroundList.setdefault('Sunny', []).append('rainy.gif')
            backgroundList.setdefault('Sunny', []).append('rain2.gif')
            backgroundList.setdefault('Sunny', []).append('rainy2.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('rain2.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('rainy2.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('rainy.gif')

    elif now > night_begin and now < morning_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny':
            backgroundList.setdefault('Partly Cloudy', []).append('nightclear.gif')
            backgroundList.setdefault('Partly Cloudy', []).append('nightclear2.gif')
            backgroundList.setdefault('Cloudy', []).append('nightclear.gif')
            backgroundList.setdefault('Cloudy', []).append('nightclear2.gif')
            backgroundList.setdefault('Mostly Cloudy', []).append('nightclear.gif')
            backgroundList.setdefault('Mostly Cloudy', []).append('nightclear2.gif')
            backgroundList.setdefault('Sunny', []).append('clearevening.gif')
            backgroundList.setdefault('Sunny', []).append('cloudy.gif')
            print("night to morning")



    else:
        print("nothing")


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
