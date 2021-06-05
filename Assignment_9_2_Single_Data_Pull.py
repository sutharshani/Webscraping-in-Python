# File:   Assignment_9_2_Single_Data_Pull.py
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

import oauth2

# Consumer API keys
API_KEY = 'X6HrY7iLtcVQdnsORQbgNQki3'
API_SECRET = 'oN6Uv5HQkktjK4KIvwwFyUk1ykkZajiy4fJU9jPc1GxZAahOhx'

# Access token & access token secret
TOKEN_KEY = '1224980085528236032-qAK1HhiXYpvau98TJQZCLV9Z1lrdNA'
TOKEN_SECRET = 'FSM91AbsC2EDbAYztcznzwEukYplSenWmeU7Od5WDa4Y8'


def oauth_req(url, key, secret, http_method="GET", post_body="",
              http_headers=None):
    """ This routine execute REST API get method and returns request response content.
    :param url: URL we want to execute
    :param key: Key of the API
    :param secret: Key secret value
    :param http_method: REST method
    :param post_body: Post body
    :param http_headers: header
    :return: return is content from REST request
    """
    consumer = oauth2.Consumer(key=API_KEY, secret=API_SECRET)  # Create consumer object using API data
    token = oauth2.Token(key=key, secret=secret)  # Create token using the key data
    client = oauth2.Client(consumer, token)   # Create client using consumer & token
    resp, content = client.request(url, method=http_method,
                                   body=post_body, headers=http_headers)  # Execute the request now
    return content   # Return content from connection


url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor'  # Set search URL
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)  # Make request and get response data

with open("./data/hashchildlabor.json", "w") as data_file:  # Open file in write mode
    data_file.write(data)  # Write data
