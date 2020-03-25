import tweepy
from keys import *

print('Hello World!')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) # this is our twitter object

mentions = api.mentions_timeline()

for mention in mentions:
        print(str(mention.id) + ' - ' + mention.text)