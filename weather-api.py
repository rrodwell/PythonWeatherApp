from datetime import datetime
from threading import Timer
import requests
import json
import threading
import datetime
import time

city = raw_input("Enter city: ")


def getWeather():
    # hardcoded api address

    api_address = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + city + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

    # JSON

    json_data = requests.get(api_address).json()

    global temperatureNow
    temperatureNow = int(json_data['query']['results']['channel']['item']['condition']['temp'])

    date = json_data['query']['results']['channel']['item']['condition']['date']

    sunrise = json_data['query']['results']['channel']['astronomy']['sunrise']
    sunset = json_data['query']['results']['channel']['astronomy']['sunset']

    print(sunrise)
    print(sunset)
    descriptionToday = json_data['query']['results']['channel']['item']['condition']['text']


    global highToday
    highToday = int(json_data['query']['results']['channel']['item']['forecast'][0]['high'])

    global highTomorrow
    highTomorrow = int (json_data['query']['results']['channel']['item']['forecast'][1]['high'])

    descriptionTomorrow = json_data['query']['results']['channel']['item']['forecast'][1]['text']


   # print(forecastTomorrow)

    # Emoji dictionary

    emojiList = {
        'Mostly Cloudy': ':cloud:',
        'Sunny': ':sunny:',
        'Cloudy': ':cloud:',
        'Mostly Sunny': ':mostly_sunny:',
        'Partly Cloudy': ':partly_sunny:',
        'Breezy': ':wind_blowing_face:',
        'Heavy Rain': ':rain_cloud:',
        'Rain': ':rain_cloud:'
    }

    now = datetime.datetime.now().time()
    morning_begin = now.replace(hour=6, minute=0, second=0, microsecond=0)
    evening_begin = now.replace(hour=14, minute=0, second=0, microsecond=0)
    night_begin = now.replace(hour=20, minute=0, second=0, microsecond=0)

    backgroundList = {}


    if now > morning_begin and now < evening_begin:

        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or'Sunny':
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
            print("Morning to evening")
            print(morning_begin)
            print(now)
            print(evening_begin)




    elif now > evening_begin and now < night_begin:
        if descriptionToday == 'Partly Cloudy' or 'Cloudy' or 'Mostly Cloudy' or 'Sunny':
            backgroundList.setdefault('Sunny', []).append('rainy.gif')
            print("evening to night")
            print(now)




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


    # print statement


def convertToCelciusToday():

    global temperatureNow
   # print (temperatureNow - 32) * 5 / 9


def convertToCelciusTomorrow():

    global highTomorrow
  #  print (highTomorrow - 32) * 5 / 9





# Slack webhook integration

#webhook_url = 'https://hooks.slack.com/services/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'
    # webhook_url = 'https://hooks.slack.com/services/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'

    # slack_data = {
    #
    #     'channel': '#pdtest',
    #     'username': 'philBot',
    #     'text': printme,
    #
    # }
    #
    # response = requests.post(
    #     webhook_url, data=json.dumps(slack_data),
    #     headers={
    #         'Content-Type': 'application/json'
    #     }
    # )
    #
    # if response.status_code != 200:
    #     raise ValueError(
    #         'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text)
    #     )





getWeather()
convertToCelciusToday()
convertToCelciusTomorrow()