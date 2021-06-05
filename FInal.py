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

from rauth.service import OAuth1Service, OAuth1Session

# Get a real consumer key & secret from: https://www.goodreads.com/api/keys
CONSUMER_KEY = 'acZeISLRqqbq2Bhdwoumw'
CONSUMER_SECRET = 'PNqu1dsKLHwps0FBgdKFuASMOKOwVMoNHgOSFurDs'

goodreads = OAuth1Service(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    name='goodreads',
    request_token_url='https://www.goodreads.com/oauth/request_token',
    authorize_url='https://www.goodreads.com/oauth/authorize',
    access_token_url='https://www.goodreads.com/oauth/access_token',
    base_url='https://www.goodreads.com/'
    )

request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

print('Visit this URL in your browser: ', request_token, request_token_secret)

authorize_url = goodreads.get_authorize_url(request_token)
print('Visit this URL in your browser: ' + authorize_url)
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = input('Have you authorized me? (y/n) ')

session = goodreads.get_auth_session(request_token, request_token_secret)


data = {'Python'}
response = session.get('Python')
print('Visit this URL in your browser: ', response.content)

