import tweepy
from .credentials import creds

auth = tweepy.OAuthHandler(creds["twitter"]["consumer_key"], creds["twitter"]["consumer_secret"])
auth.set_access_token(creds["twitter"]["access_token"], creds["twitter"]["access_secret"])
api = tweepy.API(auth)

api.verify_credentials()
print("Twitter Authentication Successful")

def post_tweet(tweet_body):
    print(tweet_body)
    api.update_status(tweet_body)