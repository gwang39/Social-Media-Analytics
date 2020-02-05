# Use Tweepy to List Followers of Page

import tweepy
import time
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

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# open file
File = open("followers.txt","w")

#Paging to deal with Rate Limit http://stackoverflow.com/questions/31000178/how-to-get-large-list-of-followers-tweepy

accountvar = "JHUAPL"



api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# Command to grab follower list

for user in tweepy.Cursor(api.followers, screen_name=accountvar).items():
	print(user.screen_name)

