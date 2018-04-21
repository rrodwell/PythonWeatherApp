from datetime import datetime
from threading import Timer
import requests
import json
import threading


def printit():

   # hardcoded api address

   api_address = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Atlanta%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

   #JSON

   json_data = requests.get(api_address).json()

   temperature = json_data['query']['results']['channel']['item']['condition']['temp']
   description = json_data['query']['results']['channel']['item']['condition']['text']
   date = json_data['query']['results']['channel']['item']['condition']['date']
   forecast = json_data['query']['results']['channel']['item']['forecast'][0]['high']

   print(description)

   #Emoji dictionary

   list1 = {
                “Mostly Cloudy': “:cloud:“,
                “Sunny': “:sunny:' ,
                “Cloudy': “:cloud:“,
                “Mostly Sunny': “:mostly_sunny:“,
                “Partly Cloudy': “:partly_sunny:“,
                “Breezy': “:wind_blowing_face:“,
                “Heavy Rain': “:rain_cloud:“,
                “Rain': “:rain_cloud:'
            }


   emoji = “'

   for k, v in list1.iteritems():
       if k == description:
           emoji = v


   # print statement

   printme = “The temperature is ' + temperature + ' degrees F and ' + description + emoji + ' in Atlanta.' + “\n The high today is ' + forecast + “.'

   #Slack webhook integration

   webhook_url = 'https://hooks.slack.com/services/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'
   #webhook_url = 'https://hooks.slack.com/services/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'

   slack_data = {

                   'channel': '#pdtest',
                   'username': 'philBot',
                   'text': printme,
                   'icon_emoji': ':waffle-fry:'
                }

   response = requests.post(
       webhook_url, data=json.dumps(slack_data),
       headers={
           'Content-Type': 'application/json'
       }
   )

   if response.status_code != 200:
       raise ValueError(
           'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text)
       )

printit()