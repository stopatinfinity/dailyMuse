import tweepy
import time
import random

from keys import *
from youtube import *

print('Welcome to Daily Muse!', flush = True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) # this is our twitter object

"""
mentions = api.mentions_timeline()
for mention in mentions:
    print(str(mention.id) + ' - ' + mention.text)
"""


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('Retrieving and replying to tweets...', flush=True)
    
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#lovesong' in mention.full_text.lower():
            print('Someone wants a love song!', flush=True)
            print('Responding back...', flush=True)
            link = random.choice(getSong('love song'))
            api.update_status('@' + mention.user.screen_name +
                    ' Here you go! ' + link, mention.id)

if __name__ == '__main__':
    while True:
        reply_to_tweets()
        time.sleep(15)