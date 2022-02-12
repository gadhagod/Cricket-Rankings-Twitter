from calendar import c
from os import getenv
from json import loads
from os import path

if(path.exists(path.join(path.dirname(path.dirname(__file__)), "creds.json"))):
    creds = loads(open(path.join(path.dirname(path.dirname(__file__)), "creds.json"), "r").read())
else:
    creds = {
        "rockset": {
            "api_token": getenv("ROCKSET_TOKEN")
        },
        "twitter": {
            "consumer_key": getenv("TWITTER_CONSUMER_KEY"),
            "consumer_secret": getenv("TWITTER_CONSUMER_SECRET"),
            "access_token": getenv("TWITTER_ACCESS_TOKEN"),
            "access_secret": getenv("TWITTER_ACCESS_SECRET")
        }   
    }