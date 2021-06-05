# File:   Kumar_Shani_DSC540_Assignment_3_2_CSV.py
# Name:   Shani Kumar
# Date:   12/15/2019
# Course: DSC-540 - Data Preparation
# Desc:   Complete the following using Python – make sure to show your work and show the values returned.
#         You can submit via your notebook or code editor, no need to export your work.
#         Submit the following for this exercise:
#         -> Using Python, import the CSV file provided under Chapter 3 in the GitHub repository using the csv library.
#            Put the data in lists and print each record on its own dictionary row
#            (Hint: Page 51-52 of Data Wrangling with Python)
# Usage:  This program is to complete assignment 3.2 requirements
# Needed to use raw_input function instead of input function. input function gives namError when used in MacOS.

import csv

csvfile = open('data/data-text.csv', 'r')  # Open the CSV file
reader = csv.DictReader(csvfile)  # Reader to read records in dictionary
file_list = []  # Init list

for row in reader:  # Loop to iterate over the rows of the csv file
    l1 = row.items()  # Creat list from dictionary
    file_list.append(l1)  # Append to store all records
    print(row)  # print record from dictionary

