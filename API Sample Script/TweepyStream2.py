# This script demonstrates collecting data from the Twitter Streaming API using the Tweepy Package

import tweepy
import simplejson as json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Keys generated from Managing Twitter Apps
# Module 6 Video provided

CONSUMER_KEY = 'RqP0xJuY2XKfZfU68vbZfsiRi'
CONSUMER_SECRET = 'WyQ7uoEIfRN4hRXHNXxcum6xhx8Jo7Dcjxa8qR073W9Cuc7pjm'
OAUTH_TOKEN = '851046331-cFjDnAWsZtz3azNQ75DleWXJuHZPtZ9DhzxlJDbK'
OAUTH_TOKEN_SECRET = '9L7FlR0yb5UxBbCKgqQbAsMTKAg1N3FhcgjO0hDbBAgta'


# open file
File = open("JHUtweets.txt","w")


class listener(StreamListener):
    def on_data(self, data):
        print(data)
        with open('JHU.json', 'a') as f:
            f.write(data)

        return True


    def on_error(self, status):
        print
        status
        print(json.dumps(tweet, indent=4))
        tweet = json.dumps(tweet, indent=4)



auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Hillary"]) # Set search term for Streaming API
