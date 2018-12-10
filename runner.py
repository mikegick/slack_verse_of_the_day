import requests
import time
import sys
import operator
import random
import string
from slackclient import SlackClient

verseURL = "https://beta.ourmanna.com/api/v1/get/?format=json"
slackToken = ''
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