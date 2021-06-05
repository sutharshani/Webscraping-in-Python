# File:   Assignment_6_2_data_format.py
# Name:   Shani Kumar
# Date:   01/28/2020
# Course: DSC-540 - Data Preparation
# Desc:   Data Formats Readable  –
#         -> Using the same dataset as the above example (mn.csv and mn-headers.csv),
#         use the format method to make output human readable.
# Note:   Using output from 6.2 exercise part
# Usage:  This program is to complete assignment 6.2 requirements
from csv import DictReader

mn_file = open('mn_fixed.csv', 'r')      # open input file (in format fixed layout)
data_reader = DictReader(mn_file)        # read in the file now

data_rows = [d for d in data_reader]     # get row data

print("Cleaned data:\n{}".format(data_rows[0].items()))  # print the data items

for x in data_rows[0].items():   # Loop through the first record on CSV file
    print("Question: {}\nAnswer: {}".format(x[0], x[1])) # print the questions and answers in readable format
