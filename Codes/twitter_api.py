#Posting a tweet programmatically using Python program

import tweepy

CONSUMER_KEY = "fdsfsdgsdg" #"The key that you got tomorrow from your twitter account"
CONSUMER_SECRET = "bdfbdfg"  # "The consumer secret"

ACCESS_KEY = "gfdgsg"   #"Access key that we created from our respective accounts in the end"
ACCESS_SECRET = "fgsgsfg"   #"Access secret"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api=tweepy.API(auth)
api.update_status('Test tweet 2!')
