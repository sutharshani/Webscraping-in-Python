# File:   Kumar_Shani_DSC540_Assignment_3_2_XML.py
# Name:   Shani Kumar
# Date:   12/15/2019
# Course: DSC-540 - Data Preparation
# Desc:   Complete the following using Python – make sure to show your work and show the values returned.
#         You can submit via your notebook or code editor, no need to export your work.
#         Submit the following for this exercise:
#         -> Using Python, import the XML file provided in the GitHub repository under Chapter 3.
#            Print each record in its own dictionary row (Hint: page 64 of Data Wrangling with Python).
# Usage:  This program is to complete assignment 3.2 requirements
# Needed to use raw_input function instead of input function. input function gives namError when used in MacOS.

from xml.etree import ElementTree as ET

tree = ET.parse('data/data-text.xml')  # Read the XML data from file.
root = tree.getroot()  # Get the root of XML data

data = root.find('Data')  # search for sub element 'Data'

all_data = []  # Start with empty list

for observation in data:  # iterate over all observations
    record = {}  # Start with empty dict
    for item in observation:  # iterate over each item in observation

        lookup_key = list(item.attrib.keys())[0]  # point to attribute key to check numeric or code

        if lookup_key == 'Numeric':  # Here checking for numeric
            rec_key = 'NUMERIC'  # say numeric
            rec_value = item.attrib['Numeric']  # Save value
        else:
            rec_key = item.attrib[lookup_key]  # Set key
            rec_value = item.attrib['Code']  # Save value

        record[rec_key] = rec_value  # set value now
    all_data.append(record)  # append the record to list

print(all_data)  # print all records
