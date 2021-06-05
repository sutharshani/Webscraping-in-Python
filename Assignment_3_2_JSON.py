# File:   Kumar_Shani_DSC540_Assignment_3_2_JSON.py
# Name:   Shani Kumar
# Date:   12/15/2019
# Course: DSC-540 - Data Preparation
# Desc:   Complete the following using Python – make sure to show your work and show the values returned.
#         You can submit via your notebook or code editor, no need to export your work.
#         Submit the following for this exercise:
#         -> Using Python, import the JSON file provided in the GitHub repository under Chapter 3.
#            Print each record on its own dictionary row (Hint: page 53-54 of Data Wrangling with Python).
# Usage:  This program is to complete assignment 3.2 requirements
# Needed to use raw_input function instead of input function. input function gives namError when used in MacOS.

import json

json_data = open('data/data-text.json').read()  # Open and read json file

data = json.loads(json_data)  # Convert JSON message in dictionary

for item in data:  # Iterate until all items in dictionary
    print(item)  # print record
