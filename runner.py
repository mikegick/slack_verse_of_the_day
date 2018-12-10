import requests
import time
import sys
import operator
import random
import string
import os
import json
import datetime
from slackclient import SlackClient

verseURL = "https://beta.ourmanna.com/api/v1/get/?format=json"
with open(os.path.join(os.path.dirname(os.path.realpath('__file__')) + "\config\settings.json")) as settings:
    jsonSettings = json.load(settings)
#--------------------------------------------------------------------------------------------------------------------------|
#DeprecationWarning: Slack Tokens are aimed to be replaced in version 2.0 of this app which will aim to use 0Auth2 instead.|
#0Auth2 information will be stored in credentials.json in the future                                                       |
    slackToken = jsonSettings["slackToken"] #                                                                       |
#--------------------------------------------------------------------------------------------------------------------------|
    channelsToPostTo = jsonSettings["channelList"]
	timeToPost = jsonSettings["postTime"]
sc = SlackClient(slackToken)


while(True):
    dayAndTime = datetime.datetime.now()
    
    if(dayAndTime.hour == timeToPost):
        r = requests.get(url = verseURL) 
        data = r.json()
        verse = "\"" + data["verse"]["details"]["text"] + "\" -" + data["verse"]["details"]["reference"]
        
        for channel in channelsToPostTo:
            sc.api_call(
              "chat.postMessage",
              channel=channel,
              text=verse,
              username="Verse of the Day"
            )
        time.sleep(86300)
    else:
        time.sleep(49)