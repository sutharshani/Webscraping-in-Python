# File:   Assignment_9_2_Twitter_Streaming.py
# Name:   Shani Kumar
# Date:   02/09/2020
# Course: DSC-540 - Data Preparation
# Desc:   Practice pulling data from Twitter publicly available API
#         -> Create a Twitter API Key and Access Token
#         -> Do a single data pull from Twitter REST API
#         -> Execute multiple queries at a time from Twitter REST API
#         -> Do a data pull from Twitter Streaming API
# Usage:  This program is to complete assignment 9.2 requirements
#         Also web-page layout got changed to solution is little bit different from text book.
# Import required packages

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

# Consumer API keys
API_KEY = 'X6HrY7iLtcVQdnsORQbgNQki3'
API_SECRET = 'oN6Uv5HQkktjK4KIvwwFyUk1ykkZajiy4fJU9jPc1GxZAahOhx'

# Access token & access token secret
TOKEN_KEY = '1224980085528236032-qAK1HhiXYpvau98TJQZCLV9Z1lrdNA'
TOKEN_SECRET = 'FSM91AbsC2EDbAYztcznzwEukYplSenWmeU7Od5WDa4Y8'


class Listener(StreamListener):   # Subclass streamlistener class to override on_data method

    def on_data(self, data):   # Define on_data method
        print data  # print stream data
        return True  # Return true


auth = OAuthHandler(API_KEY, API_SECRET)  # Create auth object to handle authentication
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)  # Provide access details

stream = Stream(auth, Listener())   # Setup stream by auth and listener
stream.filter(track=['Child'])  # Filter stream with Child

