import tweepy
import requests
import os

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

account = "cravedcuddle"

tweets = api.user_timeline(screen_name=account, count=200, include_entities=True, tweet_mode="extended")

for tweet in tweets:
    if "media" in tweet.entities:
        for media in tweet.entities["media"]:
            media_url = media["media_url"]
            file_extension = media_url.split(".")[-1]
            file_name = f"{tweet.id}_{media['id']}.{file_extension}"
            file_path = os.path.join("downloads", file_name)
            response = requests.get(media_url)
            with open(file_path, "wb") as file:
                file.write(response.content)