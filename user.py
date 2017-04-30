from __future__ import print_function
import getopt
import logging
import os
import sys
# import traceback
# third-party: `pip install tweepy`
import tweepy
f  = open('tweets.txt','a')
o = open('onlytext.txt','a')
idfile = "tt.txt"
CONSUMER_KEY = 'KHLvI76mtLlWNCQGxQa9bwerY'
CONSUMER_SECRET = 'XkomKmVm2kzo6EZKPXLyjcLSzTaBjqkcpCYM4DlIPls9SqEcAD'
OAUTH_TOKEN = '3131507693-mp7VtRHFLB4nddMbobTh5y7yBUQFzGTZTKKhOMg'
OAUTH_TOKEN_SECRET = 'zwSvFsUtpyA1fMQZcu7q63CpUtIznuKQYH8kj0bE54auU'

logging.basicConfig(level=logging.WARN)
global Logger
Logger = logging.getLogger('get_tweets_by_id')



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 0
for follower in tweepy.Cursor(api.search,  q="Giraffes",since="2015-10-10", until="2015-10-11",count=100).items():
	count +=1
	print (follower)
	print ("\n\n\n")
print (count)