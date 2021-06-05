# File:   Assignment_6_2_headers.py
# Name:   Shani Kumar
# Date:   01/26/2020
# Course: DSC-540 - Data Preparation
# Desc:   Fixing Labels/Headers –
#         -> Create a new dictionary for each row to create a new array.
#         -> If you don’t want to use the method outlined in the example on page 155-156 Data Wrangling with Python,
#         you could also use Zipping Questions and Answers as a method (page 157-163 Data Wrangling with Python).
# Usage:  This program is to complete assignment 6.2 requirements
import csv

mnCsvFile = open('mn.csv', 'r')    # Open the input file
headerFile = open('mn_headers.csv', 'r')  # Open header file

dataReader = csv.DictReader(mnCsvFile)  # define file reader for mn file
headerReader = csv.DictReader(headerFile)  # define header filer reader

dataRows = [d for d in dataReader]  # pull records in python dictionary
headerRows = [h for h in headerReader] # pull records in python dictionary
new_rows = []   # Empty list to get cleaned rows

for data_dict in dataRows:   # Loop through all data rows
    new_row = {}   # new dictionary for each row
    for dkey, dval in data_dict.items():   # loop though for each key and value in dictionary
        for header_dict in headerRows:  # Loop through all header rows
            if dkey in header_dict.values():  # Look for matching row
                new_row[header_dict.get('Label')] = dval   # append row to dictionary
        new_rows.append(new_row)  # Append new cleaned data

with open('mn_fixed.csv', 'w', newline='') as mnFixed:  # Write updated data
    dict_writer = csv.DictWriter(mnFixed, new_rows[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(new_rows)

print("Fixed data:\n{}".format(new_rows[0]))  # Print fixed data record
