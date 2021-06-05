# File:   Assignment_6_2_date_format.py
# Name:   Shani Kumar
# Date:   01/28/2020
# Course: DSC-540 - Data Preparation
# Desc:   Date Formatting –
#         -> Format the dates to determine when the interview started and ended.
# Note:   Using output from 6.2 exercise part
# Usage:  This program is to complete assignment 6.2 requirements

from csv import DictReader
from datetime import datetime
import itertools


def calulateDate(col_data, startTimeFlag):
    """ This method will calculate the start/end time and return back the time in python datetime object
    :param col_data: input data containing date value.
    :param startTimeFlag: input data containing time value.
    :return: date and time string
    """
    if startTimeFlag:
        hr_index = 11
        min_index = 12
    else:
        hr_index = 13
        min_index = 14

    time_str = '{}/{}/{} {}:{}'.format(
        col_data[6][1],
        col_data[5][1],
        col_data[7][1],
        col_data[hr_index][1],
        col_data[min_index][1],
    )

    time = datetime.strptime(time_str, '%m/%d/%Y %H:%M')   # format data & time in string
    return time


mn_file = open('mn_fixed.csv', 'r')  # Open input file
data_reader = DictReader(mn_file)    # Read input file

data_rows = [d for d in data_reader]    # get row data

print("Cleaned data:\n{}\n".format(data_rows[0].items()))  # Print the row data in formatted layout

for idx, x in enumerate(itertools.islice(data_rows[0].items(), 0, 20)):
    print("At index {}, data = {}".format(idx, x))  # Lets look at data

data = list(data_rows[0].items())  # get in list now

startTime = calulateDate(data, True)  # calculate start date
endTime = calulateDate(data, False)   # calculate end date

print("\nFor cluster number: {}, interview number: {}, started at: {} and ended at: {}".format(
    data[0][1],
    data[4][1],
    startTime,
    endTime
))
