# File:   Assignment_7_2_importing_exploring.py
# Name:   Shani Kumar
# Date:   01/26/2020
# Course: DSC-540 - Data Preparation
# Desc:   Importing Data –
#         Create a function to take an empty list, iterate over the columns and create a full list of all the column
#         types for the dataset. Then load into agate table – make sure to clean the data if you get an error.
#
#         Exploring Table Functions –
#         -> Which countries have the highest rates of child labor?
#         -> Which countries have the most girls working?
#         -> What is the average percentage of child labor in cities?
#         -> Find a row with more than 50% of rural child labor.
#         -> Rank the worst offenders in terms of child labor percentages by country.
#         -> Calculate the percentage of children not involved in child labor.
#
#         Charting with matplotlib –
#         -> Chart the perceived corruption scores compared to the child labor percentages.
#         -> Chart the perceived corruption scores compared to the child labor percentages
#            using only the worst offenders.
# Usage:  This program is to complete assignment 7.2 requirements


import xlrd
import agate
from xlrd.sheet import ctype_text
import json
import matplotlib.pyplot as plt

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


def reverse_percent(row):
    return 100 - row['Total (%)']


def get_country(country_row):
    return country_dict.get(country_row['Country / Territory'].lower())


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


def highest_rates(row):
    if row['Total (%)'] > cl_mean and row['CPI 2013 Score'] < cpi_mean:
        return True
    return False


table = get_cl_table()

most_egregious = table.order_by('Total (%)', reverse=True).limit(10)  # top 10 countries with highest child labor
print("\nCountries with highest child labor: ")
for r in most_egregious.rows:
    print("{} - {}".format(r[0], r[1]))  # print result

female_data = table.where(lambda r: r['Female'] is not None)  # get girl data
most_females = female_data.order_by('Female', reverse=True).limit(10)  # top 10 countries with highest girl labor
print("\nTop 10 countries with highest girl labor:")
for r in most_females.rows:
    print("{} - {}".format(r[0], r['Female']))  # print result

has_por = table.where(lambda r: r['Place of residence (%) Urban'] is not None)  # remove empty data
print("\nAverage % of child labor in cities: {}".
      format(has_por.aggregate(agate.Mean('Place of residence (%) Urban'))))  # print result average% of child labour

first_match = has_por.find(lambda x: x['Rural'] > 50)  # Find a row with more than 50 % of rural child labor
print("\nFirst row with more than 50% of rural child labor is - {}".
      format(first_match['Countries and areas']))

print("\nList of top 20 worst offenders: ")  # Rank the worst offenders in terms of child labor percentages by country

top_ranked = table.compute([('Total Child Labor Rank', agate.Rank('Total (%)', reverse=True)), ])
for r in top_ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print("{} - {}%, {}".format(r[0], r['Total (%)'], r['Total Child Labor Rank']))  # print result

# Get percentage of children not involved in child labor
print("\nList of top 20 countries with % of children not participating in labor:")
ranked = table.compute([('Children not working (%)', agate.Formula(number_type, reverse_percent)), ])
ranked = ranked.compute([('Total Child Labor Rank', agate.Rank('Children not working (%)', reverse=True)), ])

for r in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print("{} - {}%, {}".format(r[0], r['Total (%)'], r['Total Child Labor Rank']))

# ---------------------------------------------------------------------------------------- #

print("\n Charting with matplotlib ")

cl_table = table  # get country table for child labour
cpi_table = get_cpi_table()  # get cpi data

cpi_and_cl = cpi_table.join(ranked, 'Country / Territory', 'Countries and areas', inner=True)  # join both data table

file = open('data/earth.json', 'r')
country_json = json.loads(file.read())
file.close()
country_dict = {}
for dct in country_json:
    country_dict[dct['name']] = dct['parent']

cpi_and_cl = cpi_and_cl.compute([('continent', agate.Formula(text_type, get_country))])
africa_cpi_cl = cpi_and_cl.where(lambda x: x['continent'] == 'africa')
africa_cpi_cl.print_table()

# Plot the chart for perceived corruption scores compared to the child labor percentages.
plt.plot(africa_cpi_cl.columns['CPI 2013 Score'], africa_cpi_cl.columns['Total (%)'])
plt.xlabel('CPI Score - 2013')
plt.ylabel('Child Labor Percentage')
plt.title('CPI & Child Labor Correlation')
plt.show()

cl_mean = africa_cpi_cl.aggregate(agate.Mean('Total (%)'))
cpi_mean = africa_cpi_cl.aggregate(agate.Mean('CPI 2013 Score'))

highest_cpi_cl = africa_cpi_cl.where(lambda x: highest_rates(x))

# Plot the chart for highest offenders
plt.plot(highest_cpi_cl.columns['CPI 2013 Score'], highest_cpi_cl.columns['Total (%)'])
plt.xlabel('CPI Score - 2013')
plt.ylabel('Child Labor Percentage')
plt.title('CPI & Child Labor Correlation - Highest Offenders')
plt.show()
