# This repository does not hold the entire source code for weatherful bot, it serves to show proof of concept
# Critical code is omitted from this repository
import tweepy
import logging


class TwitterClient:
    def __init__(self, bearer_token, c_key, c_secret, a_token, a_secret):
        self.api = tweepy.API(self.auth)
        logging.basicConfig(level=logging.INFO)

    def create_tweet(self, text):
        try:
            self.client.create_tweet(text=text)
        except tweepy.TweepyException as e:
            print(e)
