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
idfile = "tid_to_uid.txt"
CONSUMER_KEY = 'KHLvI76mtLlWNCQGxQa9bwerY'
CONSUMER_SECRET = 'XkomKmVm2kzo6EZKPXLyjcLSzTaBjqkcpCYM4DlIPls9SqEcAD'
OAUTH_TOKEN = '3131507693-mp7VtRHFLB4nddMbobTh5y7yBUQFzGTZTKKhOMg'
OAUTH_TOKEN_SECRET = 'zwSvFsUtpyA1fMQZcu7q63CpUtIznuKQYH8kj0bE54auU'

logging.basicConfig(level=logging.WARN)
global Logger
Logger = logging.getLogger('get_tweets_by_id')

def get_tweet_id(line):
    '''
    Extracts and returns tweet ID from a line in the input.
    '''
    (tweet_id) = str(line.split(' ')[0])
    (user_id) = str(line.split(' ')[1])
    # (_tag, _search, tweet_id) = tagid.split(':')
    return tweet_id,user_id

def get_tweets_single(twapi, idfilepath):
    with open(idfilepath, 'rb') as idfile:
    	x=0
        for line in idfile:
            tweet_id = get_tweet_id(line)[0]
            user_id = get_tweet_id(line)[1]
            Logger.debug('Fetching tweet for ID %s', tweet_id)
            try:
                tweet = twapi.get_status(tweet_id)
                f.write('%s^^^%s *** %s ~~ %s &&\n\n' % (user_id,tweet_id, tweet.text.encode('UTF-8'),tweet.created_at))
                o.write(tweet.text.encode('UTF-8')+'\n\n')
            except tweepy.TweepError as te:
                Logger.warn('Failed to get tweet ID %s: %s', tweet_id, te.response.text)

            x+=1
            print (x)
                # traceback.print_exc(file=sys.stderr)
        # for
    # with

def get_tweet_list(twapi, idlist):

    tweets = twapi.statuses_lookup(id_=idlist, include_entities=False, trim_user=True)
    for tweet in tweets:
    	f.write('%s \n %s \n~ %s \n\n' % (tweet.id, tweet.text.encode('UTF-8'), tweet.created_at))


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)
get_tweets_single(api, idfile)
f.close()