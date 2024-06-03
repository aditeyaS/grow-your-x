from ..errors.ApiKeyError import ApiKeyError
import os
import tweepy

class Twitter:
    def __init__(self) -> None:
        API_KEY = os.getenv("X_API_KEY")
        if not API_KEY:
            raise ApiKeyError("Missing X_API_KEY")
        API_KEY_SECRET = os.getenv("X_API_KEY_SECRET")
        if not API_KEY_SECRET:
            raise ApiKeyError("Missing API_KEY_SECRET")
        ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
        if not ACCESS_TOKEN:
            raise ApiKeyError("Missing ACCESS_TOKEN")
        ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
        if not ACCESS_TOKEN_SECRET:
            raise ApiKeyError("Missing ACCESS_TOKEN_SECRET")
        self.client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_KEY_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
    
    def tweet(self, generated_tweet: str) -> None:
        self.client.create_tweet(text=generated_tweet)