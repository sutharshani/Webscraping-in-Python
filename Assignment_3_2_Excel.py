# File:   Kumar_Shani_DSC540_Assignment_3_2_Excel.py
# Name:   Shani Kumar
# Date:   12/15/2019
# Course: DSC-540 - Data Preparation
# Desc:   Complete the following using Python – make sure to show your work and show the values returned.
#         You can submit via your notebook or code editor, no need to export your work.
#         Submit the following for this exercise:
#         -> Using Python, import the Excel file provided in the GitHub repository under Chapter 4.
#            Print each record in its own dictionary row. (Hint: page 85-88 of Data Wrangling with Python).
# Usage:  This program is to complete assignment 3.2 requirements
# Needed to use raw_input function instead of input function. input function gives namError when used in MacOS.

import xlrd
import pprint

book = xlrd.open_workbook("./data/SOWC 2014 Stat Tables_Table 9.xlsx")  # Open the excel workbook

sheet = book.sheet_by_name("Table 9 ")  # open sheet 'Table 9'

data = {}  # Start with empty dict
for i in range(14, sheet.nrows):

    # Start at 14th row, because that is where the countries begin
    row = sheet.row_values(i)

    country = row[1]

    data[country] = {  # Expand the dictionary here
        'child_labor': {  # Create child_labor key
            'total': [row[4], row[5]],  # set and respective value
            'male': [row[6], row[7]],  # set and respective value
            'female': [row[8], row[9]],  # set and respective value
        },
        'child_marriage': {  # Create child_labor key
            'married_by_15': [row[10], row[11]],  # set and respective value
            'married_by_18': [row[12], row[13]],  # set and respective value
        }
    }

    if country == "Zimbabwe":  # Exit the loop when it is Zimbabwe
        break

pprint.pprint(data)  # print all data
