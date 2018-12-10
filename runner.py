import requests
import time
import sys
import operator
import random
import string
from slackclient import SlackClient

verseURL = "https://beta.ourmanna.com/api/v1/get/?format=json"
settings = open("settings.json", "r").json()
#--------------------------------------------------------------------------------------------------------------------------|
#DeprecationWarning: Slack Tokens are aimed to be replaced in version 2.0 of this app which will aim to use 0Auth2 instead.|
#0Auth2 information will be stored in credentials.json in the future                                                       |
slackToken = settings["slackToken"] #                                                                                      |
#--------------------------------------------------------------------------------------------------------------------------|
sc = SlackClient(slackToken)
channelToPostTo = "general"

while(True):
    
    r = requests.get(url = verseURL) 
    data = r.json()
    verse = "\"" + data["verse"]["details"]["text"] + "\" -" + data["verse"]["details"]["reference"]
    
    
    sc.api_call(
      "chat.postMessage",
      channel=channelToPostTo,
      text=verse,
      username="Verse of the Day"
    )
    time.sleep(86400)