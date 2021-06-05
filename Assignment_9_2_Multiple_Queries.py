# File:   Assignment_9_2_Multiple_Queries.py
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

import tweepy
import dataset

# Consumer API keys
API_KEY = 'X6HrY7iLtcVQdnsORQbgNQki3'
API_SECRET = 'oN6Uv5HQkktjK4KIvwwFyUk1ykkZajiy4fJU9jPc1GxZAahOhx'

# Access token & access token secret
TOKEN_KEY = '1224980085528236032-qAK1HhiXYpvau98TJQZCLV9Z1lrdNA'
TOKEN_SECRET = 'FSM91AbsC2EDbAYztcznzwEukYplSenWmeU7Od5WDa4Y8'


def store_tweet(item):
    """This routine stores sweet data in tweets table"""
    db = dataset.connect('sqlite:///data_wrangling.db')  # connect to database
    db.create_table('tweets', primary_id=False)
    table = db['tweets']  # Create or Access table tweets
    item_json = item._json.copy()  # Copy all data
    for k, v in item_json.items():  # loop through all the items
        if isinstance(v, dict):  # Is there value in the form of dictionary ?
            item_json[k] = str(v)  # Convert dictionary data into string
    table.insert(item_json)  # insert result data


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)  # Create auth object to handle authentication
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)   # Provide access details

api = tweepy.API(auth)  # Create tweety API object to manage the RESTFul API requests.

query = '#childlabor'  # Setup query
cursor = tweepy.Cursor(api.search, q=query, lang="en")  # Create cursor with query with english results

for page in cursor.pages():  # Loop through all the pages in cursor
    for item in page:   # loop through all the items in page
        store_tweet(item)  # Go store the tweet data
