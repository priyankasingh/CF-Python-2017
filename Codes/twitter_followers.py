#Finding number of followers of a particular twitter user

import tweepy
import time

CONSUMER_KEY = "The key that you got tomorrow from your twitter account"
CONSUMER_SECRET = "The consumer secret"

ACCESS_KEY = "Access key that we created from our respective accounts in the end"
ACCESS_SECRET = "Access secret"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api=tweepy.API(auth)

ids=[]
for page in tweepy.Cursor(api.followers_ids, screen_name="CodeFirstGirls").pages():
    ids.extend(page)
    time.sleep(60)

print("Number of followers for this user: ",len(ids))
