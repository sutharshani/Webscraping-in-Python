# File:   Assignment_8_2_connect_internet.py
# Name:   Shani Kumar
# Date:   02/03/2020
# Course: DSC-540 - Data Preparation
# Desc:   Connect to Internet –
#         Connect to the Internet using Python Library urllib (Data Wrangling with Python? pg 298-300),
#         follow the example in the book to connect to the same website or a different website and submit your code.
# Note:   This code uses Python 3.7 so it have code little be different then whats there in textbook.
# Usage:  This program is to complete assignment 8.2 requirements


# Import required packages
import urllib.request
import urllib.parse
import requests

yahoo = urllib.request.urlopen('https://in.yahoo.com/?p=us')   # Create url open request
yahoo = yahoo.read()   # Read data from the page
print("-----------------Content first 200----------------")
print(yahoo[:200])  # Print first 200 bytes from the page

url = 'https://in.search.yahoo.com/search?p='  # base url for yahoo search
url_with_query = url + urllib.parse.quote_plus('python world')  # setup search string

web_search = urllib.request.urlopen(url_with_query)  # Create url open request
web_search = web_search.read()  # Read data from the page
print("-----------------Content first 200----------------")
print(web_search[:200]) # Print first 200 bytes from the page

google = requests.get('http://google.com') # setup GET request for the URL

print("-----------------Status Code----------------")
print(google.status_code)  # print get request return status
print("-----------------Content first 200----------------")
print(google.content[:200])  # print first 200 bytes
print("-----------------Header----------------")
print(google.headers)  # print header data
print("-----------------Cookies----------------")
print(google.cookies.items())  # print cookies data

