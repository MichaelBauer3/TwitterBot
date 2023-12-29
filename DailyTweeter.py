import tweepy
import requests
import json
import re

# Insert your Twitter API keys here
consumerKey = "72NUmAaOFWu5wZLjfp4ziEXnd"
consumerSecret = "r691akPVUb5Ksbb2TKVNiukTckCrWblmXZuds2IsYdmrFnBL5S"
accessToken = "1610909110186164224-97o5hd8KeLGzQffhLmWBAzRuMYTTZX"
accessTokenSecret = "0XUTCFhfSEt5z33o5z8Dg3L5dO6PXRK9570Ojr5JnwzQ6"

# API endpoint for jokes
url = "https://icanhazdadjoke.com/"

headers = {'Accept': 'application/json'}

auth = tweepy.OAuth1UserHandler(consumerKey, consumerSecret, accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Get the last tweet posted by the account
last_tweet = api.user_timeline(count=1)[0]
last_tweet_text = last_tweet.text

# Find the number in the last tweet and increment it by one
match = re.search(r'\d+', last_tweet_text)
if match:
    num = int(match.group(0))
    num += 1
else:
    num = 99

# Get a new joke
response = requests.get(url, headers=headers)
data = json.loads(response.text)
joke = data["joke"]

# Construct the new tweet with the updated number and the new joke
string = "Daily Tweet #" + str(num) + " at @K18boss2 & @KurtisWalker17: " + "\n\n" + joke

# Post the tweet
api.update_status(string)

print("Success! Tweet was sent.")