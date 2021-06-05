# File:   Assignment_8_2_Beautiful_Soup.py
# Name:   Shani Kumar
# Date:   02/03/2020
# Course: DSC-540 - Data Preparation
# Desc:   Beautiful Soup –
#         Reading a Web Page with Beautiful Soup – following the example starting on page 300-304 of
#         Data Wrangling with Python, use the Beautiful Soup Python library to scrap a web page.
#         The result should be data and output in an organized format. Each of the data entries should be in its
#         own dictionary with matching keys.
# Note:   This code uses Python 3.7 so it have code little be different then whats there in textbook.
# Usage:  This program is to complete assignment 8.2 requirements
#         Also web-page layout got changed to solution is little bit different from text book.
# Import required packages
from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.enoughproject.org/take_action')   # setup url get request

# print(page.content)
bs = BeautifulSoup(page.content, 'html.parser')  # Start parsing with BS
ta_divs = bs.find_all("div", class_="wpb_text_column wpb_content_element")  # list to div required

# Initialize required fields
all_data = []
index = 1

for header in bs.find_all('h6'):  # loop through all headers
    data_dict = {'title': header.text,   # setup title text
                 'link': header.a.get('href'),  # setup title url
                 'about': ta_divs[index].find_next('p').get_text()} # setup title description
    all_data.append(data_dict)  # Append to dictionary
    index += 1

for dict in all_data:  # loop through all element
    print(dict)  # print data

