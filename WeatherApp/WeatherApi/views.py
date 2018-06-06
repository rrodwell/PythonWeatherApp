from django.shortcuts import render
from .forms import LocationSearchForm
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

    # search_location(request)
    location = ''
    
    if location == '':
        location = 'Atlanta'
    
    api_address = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'+ location +'%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

    # JSON

    json_data = requests.get(api_address).json()
    #print("JSON:",json_data)

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


    weekly_forecast = [
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][1]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][1]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][1]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][1]['text'],
        },
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][2]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][2]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][2]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][2]['text'],
        },
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][3]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][3]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][3]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][3]['text'],
        },
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][4]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][4]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][4]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][4]['text'],

        },
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][5]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][5]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][5]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][5]['text'],
        },
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][6]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][6]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][6]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][6]['text'],
        },
        {
            "day": json_data['query']['results']['channel']['item']['forecast'][7]['day'],
            "high": int(json_data['query']['results']['channel']['item']['forecast'][7]['high']),
            "low": int(json_data['query']['results']['channel']['item']['forecast'][7]['low']),
            "text": json_data['query']['results']['channel']['item']['forecast'][7]['text'],
        }
    ]
   # print(forecastTomorrow)
    print(descriptionToday)

    # Emoji dictionary

    now = datetime.datetime.now().time()
    morning_begin = now.replace(hour=6, minute=0, second=0, microsecond=0)
    evening_begin = now.replace(hour=17, minute=30, second=0, microsecond=0)
    night_begin = now.replace(hour=20, minute=0, second=0, microsecond=0)
    night_end = now.replace(hour=23, minute=0, second=0, microsecond=0)
    dawn = now.replace(hour=1, minute=0, second=0, microsecond=0)


    backgroundList = {}


    if now >= morning_begin and now < evening_begin:

        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or'Sunny' or ' Mostly Sunny' or 'Thunderstorms':
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

    elif now >= evening_begin and now < night_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny' or 'Most Sunny':
            backgroundList.setdefault('Sunny', []).append('clearevening.gif')

    elif now > evening_begin and now < night_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny' or 'Most Sunny' or 'Thunderstorms':
            backgroundList.setdefault('Sunny', []).append('clearevening.gif')




    elif now >= evening_begin and now < night_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny' or 'Most Sunny':

            backgroundList.setdefault('Sunny', []).append('rainy.gif')
            backgroundList.setdefault('Sunny', []).append('rain2.gif')
            backgroundList.setdefault('Sunny', []).append('rainy2.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('rain2.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('rainy2.gif')
            backgroundList.setdefault('Mostly Sunny', []).append('rainy.gif')
            backgroundList.setdefault('Cloudy', []).append('clearevening.gif')


    elif now >= night_begin and now <= night_end:
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

    elif now >= dawn and now < morning_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny':
            backgroundList.setdefault('Partly Cloudy', []).append('nightclear.gif')
            backgroundList.setdefault('Partly Cloudy', []).append('nightclear2.gif')
            backgroundList.setdefault('Cloudy', []).append('nightclear.gif')
            backgroundList.setdefault('Cloudy', []).append('nightclear2.gif')
            backgroundList.setdefault('Mostly Cloudy', []).append('nightclear.gif')
            backgroundList.setdefault('Mostly Cloudy', []).append('nightclear2.gif')
            backgroundList.setdefault('Sunny', []).append('clearevening.gif')
            backgroundList.setdefault('Sunny', []).append('cloudy.gif')
            print("dawn to morning")



    else:
        print("nothing")


    print ("BackgroundList:",backgroundList)
    backgroundImg = ''


    for k, v in backgroundList.items():
        if k == descriptionToday:
            backgroundImg = random.choice(v)


    # print statement

    weatherUpdate = 'The temperature is ' + temperatureNow + ' degrees F and ' + descriptionToday + ' in Atlanta.' + '\n The high today is ' + highToday + '. \n Tomorrow : ' + highTomorrow + " and " + descriptionTomorrow


    sunny_desc = ['Sunny','Clear','Partly Sunny']
    mostly_sunny_desc = ['Mostly Sunny','Partly Cloudy',]
    cloudy_desc = ['Cloudy','Mostly Cloudy','Partly Cloudy','Breezy']
    rainy_desc = ['Rain','Scattered Showers','Heavy Rain']
    storm_desc = ['Thunderstorms', 'Scattered Thunderstorms']
    snow_desc = []


    weatherForecast = {
        'forecast': weatherUpdate,
        'temperature': temperatureNow,
        'background': backgroundImg,
        'weekly_forecast': weekly_forecast,
        'sunny_desc': sunny_desc,
        'mostly_sunny_desc': mostly_sunny_desc,
        'cloudy_desc': cloudy_desc,
        'rainy_desc': rainy_desc,
        'storm_desc': storm_desc,
        'snow_desc': snow_desc
    }

    print(weatherForecast)

    return render(request,'WeatherApi/index.html',context=weatherForecast)


def search_location(request):
    if request.method == 'POST':
        form = LocationSearchForm(request.POST)
        if form.is_Valid(): 
            location = HttpResponse('')
            return location
    else:
        form = LocationSearchForm()

    return render(request, 'form.html', {'form': form})