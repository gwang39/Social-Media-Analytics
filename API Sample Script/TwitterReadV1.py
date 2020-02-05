# Reading the REST API for Twitter
# credit to /html/Chapter%201%20-%20Mihttps://rawgit.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/master/ipynbning%20Twitter.html


__author__ = 'piorkja1'
import twitter
import  simplejson as json

# Keys generated from Managing Twitter Apps
# Module 6 Video provided


CONSUMER_KEY = 'RqP0xJuY2XKfZfU68vbZfsiRi'
CONSUMER_SECRET = 'WyQ7uoEIfRN4hRXHNXxcum6xhx8Jo7Dcjxa8qR073W9Cuc7pjm'
OAUTH_TOKEN = '851046331-cFjDnAWsZtz3azNQ75DleWXJuHZPtZ9DhzxlJDbK'
OAUTH_TOKEN_SECRET = '9L7FlR0yb5UxBbCKgqQbAsMTKAg1N3FhcgjO0hDbBAgta'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Set search topic

q = '#JHU'

# Set limit on count of tweets
count = 500

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)


statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(500):
    print ("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError : # No more results when next_results doesn't exist
        break

    # Setup parsing of Twittes
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
print (json.dumps(statuses[0], indent=1))

status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 100 items for each...

print (json.dumps(status_texts[0:100], indent=1))
file = open("twitterjhu.txt", "w")

file.write(json.dumps(status_texts[0:500], indent=1))

