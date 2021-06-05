# coding=utf-8
# File:   Kumar_Shani_DSC540_Assignment_4_2_PDF.py
# Name:   Shani Kumar
# Date:   12/22/2019
# Course: DSC-540 - Data Preparation
# Desc:   Follow along with the book and complete the exercise that uses the Slate library starting on page 94 until
# page 114 (Data Wrangling with Python). At the end of the exercise, the author explains that they’ve run into a
# roadblock in the code and troubleshooting is the next step. Turn in what you have completed so far with the exercise
# (make sure to show your work). For extra credit, see if you can get better results and a cleaner process working
# without having data land in the wrong columns. This is the challenge with data like a PDF – there aren’t necessarily
# the same rules that can be counted on each time and as mentioned above, sometimes manual manipulation ends up being
# the fastest way to deal with the data.
# Usage:  This program is to complete assignment 4.2 requirements

import pprint

pdf_txt = 'en-final-table9.txt'  # File to be opened
openfile = open(pdf_txt, 'r')  # Open file now
country_line = False  # Start with false
total_line = False  # Star with false
previous_line = ''  # Star with empty
countries = []  # Empty country list
totals = []  # Empty total list

# Declare multiple line country table
double_lined_countries = [
    'Bolivia (Plurinational \n',
    'Democratic People\xe2\x80\x99s \n',
    'Democratic Republic \n',
    'Lao People\xe2\x80\x99s Democratic \n',
    'Micronesia (Federated \n',
    'Saint Vincent and \n',
    'The former Yugoslav \n',
    'United Republic \n',
    'Venezuela (Bolivarian \n',
]


def switch(line, status, start, prev_line, end='\n'):
    """
    This function checks to see if a line starts/ends with a certain
    value. If the line starts/ends with that value, the status is
    set to on/off (True/False).
    """
    if line.startswith(start):
        status = True
    elif status:
        if line == end and (prev_line != 'and areas\n' and prev_line != 'total\n'):
            status = False

    return status


def cleanup(myline):
    """
    This function cleans up line data
    """
    myline = myline.strip().strip('\n')
    myline = myline.replace('\xe2\x80\x93', '-')
    myline = myline.replace('\xe2\x80\x99', '\'')
    return myline


# loop through to check each and every line for data
for line in openfile:
    if country_line:
        if previous_line in double_lined_countries:
            line = cleanup(previous_line).join(cleanup(line))
        if len(cleanup(line)) > 0:
            countries.append(cleanup(line))

    elif total_line:
        if len(line.strip('\n').strip()) > 0:
            totals.append(cleanup(line))

    country_line = switch(line, country_line, 'and areas', previous_line)  # check for country startup
    total_line = switch(line, total_line, 'total', previous_line)  # check for total startup
    previous_line = line  # set current to previous

# Print the data now
data = dict(zip(countries, totals))
pprint.pprint(data)
