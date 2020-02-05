#A simple example script to get all posts on a user's timeline.
#Originally created by Mitchell Stewart.
#<https://gist.github.com/mylsb/10294040>
#"""
import facebook
import requests


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).

    """
    print(post['message'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBAHffZC4xcjIjEgg6a0E0Lvg4zlAjy8DfUZClgeySz2WwATWJHdwqQdiAy47QZA2kFnMpZCmUQWcxNkAhFsVzpKWG9H3Usc3EHtNZAci2XYhj8x4lfnNIjZB3IDe48cH18gVmHKNLLuq3PwtEcsV1ZAZCMw9oPmpCzIzu5Kvve8ft7xN3AKsKXPMZD'
# Look at a page's profile for this example by using his Facebook id.
user = 'JohnsHopkinsEP'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break