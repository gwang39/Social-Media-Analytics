
__author__ = 'piorkja1'
# Simple PRAW Script to Read SubRedit on Hopkins
import praw
import json
file = open("reddit.txt", "w")
#r = praw.Reddit(user_agent='HNDb43YbZ4KUPg')
r = praw.Reddit(user_agent='HNDb43YbZ4KUPg')
#r = praw.Reddit(user_agent='euK8aOYsBOdRMzRUsQVt08-QITU')
for post in r.get_subreddit('JHU') \
             .get_comments(limit=200):
    print (post.author.name)
    print(post.body)
    file.write(post.body + '\n')

