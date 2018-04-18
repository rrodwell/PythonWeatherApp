from datetime import datetime
from threading import Timer
import requests
import json
import threading


def getWeather():

    printstatement = 'You might need a jacket!'
    printstatement2 = 'No jacket needed!'

    api_address = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Atlanta%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

    json_data = requests.get(api_address).json()

    weather = json_data['query']['results']['channel']['item']['condition']['temp']
    description = json_data['query']['results']['channel']['item']['condition']['text']
    date = json_data['query']['results']['channel']['item']['condition']['date']
    forecast = json_data['query']['results']['channel']['item']['forecast'][0]['high']

    print(description)

    if description == 'Mostly Cloudy':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :partly_sunny: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Cloudy':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :cloud: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Sunny':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :sunny: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Mostly Sunny':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :mostly_sunny: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Clear':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :sunny: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Heavy Rain':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :rain_cloud: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Rain':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :rain_cloud: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Light Rain':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :rain_cloud: ' + ' in Atlanta. The high today is ' + forecast + '.'

    elif description == 'Breezy':
        printme = 'The temp is ' + weather + ' degrees F and ' + description + ' :wind_blowing_face: ' + ' in Atlanta. The high today is ' + forecast + '.'

    else: 
        printme = "Description not available at this time."


    webhook_url = 'https://hooks.slack.com/services/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'

    #webhook_url = 'https://hooks.slack.com/services/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'

    slack_data = {
    'channel': '#weather',
    'username': 'weatherBot',
    'text': printme,
    'icon_emoji': ':waffle-fry:'
    }

    response = requests.post(
        webhook_url, data = json.dumps(slack_data),
        headers = {
            'Content-Type': 'application/json'
        }
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text)
        )

    return


getWeather()