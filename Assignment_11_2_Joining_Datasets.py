# coding=utf-8
# File:   Assignment_11_2_Joining_Datasets.py
# Name:   Shani Kumar
# Date:   02/23/2020
# Course: DSC-540 - Data Preparation
# Desc:   Practice joining numerous datasets – an activity you will likely run into frequently. Following the example
#         in your text that starts on page 229 – 233 of Data Wrangling with Python, work through the example to bring
#         two datasets together.
# Usage:  This program is to complete assignment 11.2 requirements
#
# Import required packages
import xlrd
import agate
from xlrd.sheet import ctype_text

text_type = agate.Text()  # define text type
number_type = agate.Number()  # define number type
boolean_type = agate.Boolean()  # define boolean type
date_type = agate.Date()  # define date type


def remove_bad_chars(val):
    """ This method remove bad character from data. If it is '-' it returns none
    :param val: input string data
    :return: input string or none
    """
    if val == '-':
        return None
    return val


def get_types(example_row):
    """
    This routine based on data in a row determines the column type
    :param example_row: input data
    :return: return column data type details
    """
    col_types = []
    for v in example_row:
        value_type = ctype_text[v.ctype]
        if value_type == 'text':
            col_types.append(text_type)
        elif value_type == 'number':
            col_types.append(number_type)
        elif value_type == 'xldate':
            col_types.append(date_type)
        else:
            col_types.append(text_type)

    return col_types


def get_cpi_table():
    """ This reads corruption data and returns corruption table
    :return: agate corruption table
    """
    workbook = xlrd.open_workbook('data/corruption_perception_index.xls')  # Read input file

    sheet = workbook.sheets()[0]  # Select 1st sheet
    titles_rows = zip(sheet.row_values(1), sheet.row_values(2))  # Select rows 4 & 5 as they have titles
    titles = [(t[0] + ' ' + t[1]).strip() for t in titles_rows]  # Clean the title
    curr_country_rows = [sheet.row_values(r) for r in range(3, sheet.nrows)]  # Extract cpi rows

    col_types = get_types(sheet.row(3))

    # Clean the country data by removing '-' in numeric columns
    cleaned_rows = []
    for row in curr_country_rows:
        cleaned_row = [remove_bad_chars(rv) for rv in row]
        cleaned_rows.append(cleaned_row)

    return agate.Table(cleaned_rows, titles, col_types)


def get_cl_table():
    """ This reads unicef data and returns cl table
    :return: agate cl table
    """

    workbook = xlrd.open_workbook('data/unicef_oct_2014.xls')  # Read input file.
    sheet = workbook.sheets()[0]  # Select first sheet
    rows_sheet = sheet.nrows  # Get number of rows in sheet

    title_rows = zip(sheet.row_values(4), sheet.row_values(5))  # get title rows

    titles_clean = [t[0] + ' ' + t[1] for t in title_rows]  # clean title
    titles_clean = [t.strip() for t in titles_clean]  # clean title
    print("Titles of the input spreadsheet file: \n{}".format(titles_clean))

    country_rows = [sheet.row_values(r) for r in range(6, 114)]  # get country data

    sample_row = sheet.row(6)  # get sample row for type
    types_col = get_types(sample_row)  # get type details

    cleaned_rows = []  # define cleaned row
    for row in country_rows:  # loop through country
        cleaned_row = [remove_bad_chars(rv) for rv in row]  # remove bad character
        cleaned_rows.append(cleaned_row)  # append result

    return agate.Table(cleaned_rows, titles_clean, types_col)  # build now cleaned table


cl_table = get_cl_table()  # get country table for child labour
cpi_table = get_cpi_table()  # get cpi data

# join both data table - matching data will be stored in cpi_and_cl
cpi_and_cl = cpi_table.join(cl_table, 'Country / Territory', 'Countries and areas', inner=True)

# Save joined data in csv file
cpi_and_cl.to_csv('data/Join_Output.csv')

