# coding=utf-8
# File:   Assignment_10_Logging.py
# Name:   Shani Kumar
# Date:   02/17/2020
# Course: DSC-540 - Data Preparation
# Desc:   Complete the following using Python – make sure to show your work and show the values returned.
#         You can submit via your notebook or code editor, no need to export your work.
#         -> Add Python logging to previous code that you have written. In your logging, include a note to yourself
#         with the area of the code writing the message so you know where the error occurred. Include your code and
#         output in your submitted assignment.
# Usage:  This program is to complete assignment 10.2 requirements
#
# Import required packages
import logging
import os
from datetime import datetime
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
    client = oauth2.Client(consumer, token)  # Create client using consumer & token

    logging.debug("SCRIPT: I'm making request and getting response!")  # write debug message
    try:
        resp, content = client.request(url, method=http_method,
                                       body=post_body, headers=http_headers)  # Execute the request now
    except Exception:
        logging.exception('SCRIPT: We had a problem with client request!')  # write exception message
        logging.error('SCRIPT: Issue with client.request() function request') # write error message

    return content  # Return content from connection


def start_logger():
    """ This routine sets up log file and configure logging setting
    :return: no return from this routine
    """
    filename = '/data/daily_report_%s.log' % datetime.strftime(datetime.now(), '%m%d%Y_%H%M%S')  # set file name
    log_filename = ''.join([os.getcwd(), filename])  # get full file name and path
    if not os.path.isfile(log_filename):  # check file exist or not
        logging.basicConfig(filename=log_filename,
                            filemode="w",
                            level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            datefmt='%m-%d %H:%M:%S')  # create new file and setup logging
    else:
        logging.basicConfig(filename=log_filename,
                            filemode="a",
                            level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            datefmt='%m-%d %H:%M:%S')  # set logging file and setup configuration


def main():
    start_logger()  # go setup logger
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor'  # Set search URL

    logging.debug("SCRIPT: I'm starting make request and get response!")
    data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)  # Make request and get response data

    try:
        logging.debug("SCRIPT: I'm starting writing twitter data!")  # write debug message
        with open("./data/hashchildlabor.json", "w") as data_file:  # Open file in write mode
            data_file.write(data)  # Write data
    except Exception:
        logging.exception('SCRIPT: We had a problem!')  # write exception message
        logging.error('SCRIPT: Issue with oauth_req() function request')  # write error message

    logging.debug('SCRIPT: All done!')  # write debug message


if __name__ == '__main__':
    main()
