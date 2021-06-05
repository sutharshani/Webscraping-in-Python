# File:   Mini_Project_6_2_Olympics_Data.py
# Name:   Shani Kumar
# Date:   01/26/2020
# Course: DSC-540 - Data Preparation
# Desc:   Mini project to cover below activities & transformations:
#         o Replace headers
#         o Format Data to a Readable Format
#         o Identify outliers and bad data
#         o Find Duplicates
#         o Conduct Fuzzy Matching
# Usage:  This program is to complete assignment 8.2 requirements.
import collections
import csv
import pandas as pd
from fuzzywuzzy import fuzz

input1 = './data/athlete_events.csv'  # the athlete data file
input2 = './data/noc_regions.csv'  # NOC data file
outputFile = './data/cleaned_olympic_data.csv'  # Cleaned output data
interestingHeaders = [
    "ID", "Name", "Sex", "Age", "Height", "Weight", "Games", "Year", "Season", "City", "Sport", "Event",
    "Medal", "NOC", "region"]  # selected header data for analysis work


def filterHeader(header):
    """This routine uses fuzzy methods to build dataset with matching headers from the interested and selected header
    :return: returns combined input data which is list of ordered dictionary
    """
    foundHeader = {}  # start with initial

    for selectedHeader in interestingHeaders:  # loop through interesting header data
        if not (selectedHeader in foundHeader.values()):  # check if already found
            for inputHeader in header:  # loop through input headers
                ratio = fuzz.token_set_ratio(selectedHeader, inputHeader)  # check for likeliness
                if 95 < ratio <= 100:  # Check if with in range to be considered matched
                    foundHeader[selectedHeader] = inputHeader
                    print("- Fuzzy compare - {} vs {} :  {}".format(selectedHeader, inputHeader, ratio))  # print result
    if len(foundHeader) == 0:  # check whether anything found ?
        print("Nothing found")  # Print if nothing found
    else:
        print("\nHeaders found in input: \n{}".format(foundHeader))  # print whatever found in input

    return foundHeader  # return found header data


def clearData(new_rows):
    """ This routine look at input data and clear the data for better analysis result
    :param new_rows: input data that needs to be cleaned
    :return: returns cleaned data
    """
    df = pd.DataFrame(new_rows)  # Convert in pandas data frame
    df = df.drop_duplicates()  # remove duplicate records
    df['ID'] = df['ID'].astype(int)  # change ID field type as integer
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Set field as numeric
    df['Height'] = pd.to_numeric(df['Height'], errors='coerce')  # Set field as numeric
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')  # Set field as numeric
    df['Year'] = df['Year'].astype(int)  # Set field as integer

    event_weights = pd.DataFrame(df.groupby('Event', as_index=False)['Weight'].mean())  # get mean weight under event
    df.Weight = df.Weight.mask(df.Weight.eq(0)).fillna(
        df.Event.map(event_weights.set_index('Event').Weight))  # set weight from mean weight

    event_heights = pd.DataFrame(df.groupby('Event', as_index=False)['Height'].mean())  # get mean height under event
    df.Height = df.Height.mask(df.Height.eq(0)).fillna(
        df.Event.map(event_heights.set_index('Event').Height))  # set height from mean weight

    event_ages = pd.DataFrame(df.groupby('Event', as_index=False)['Age'].mean())  # get mean age under event
    df.Age = df.Age.mask(df.Age.eq(0)).fillna(
        df.Event.map(event_ages.set_index('Event').Age))  # set age from mean weight

    men_weight = df['Weight'].loc[df['Sex'] == 'M'].mean()  # get mean weight for male
    df['Weight'].loc[df['Sex'] == 'M'] = df['Weight'].loc[df['Sex'] == 'M'].fillna(men_weight)  # set mean weight

    women_weight = df['Weight'].loc[df['Sex'] == 'F'].mean()  # get mean weight for female
    df['Weight'].loc[df['Sex'] == 'F'] = df['Weight'].loc[df['Sex'] == 'F'].fillna(women_weight)  # set mean weight

    men_height = df['Height'].loc[df['Sex'] == 'M'].mean()  # get mean height for male
    df['Height'].loc[df['Sex'] == 'M'] = df['Height'].loc[df['Sex'] == 'M'].fillna(men_height)  # set mean height

    women_height = df['Height'].loc[df['Sex'] == 'F'].mean()  # get mean height for female
    df['Height'].loc[df['Sex'] == 'F'] = df['Height'].loc[df['Sex'] == 'F'].fillna(women_height)  # set mean height

    men_age = df['Age'].loc[df['Sex'] == 'M'].mean()  # get mean age for male
    df['Age'].loc[df['Sex'] == 'M'] = df['Age'].loc[df['Sex'] == 'M'].fillna(men_age)  # set mean age for male

    women_age = df['Age'].loc[df['Sex'] == 'F'].mean()  # get mean age for female
    df['Age'].loc[df['Sex'] == 'F'] = df['Age'].loc[df['Sex'] == 'F'].fillna(women_age)  # set mean age for female

    df['notes'] = df['notes'].fillna('NONE')  # replace NA with NONE
    df['region'] = df['region'].fillna(df['Team'])  # Set NA region with value from Team
    df['Medal'] = df['Medal'].replace({'NA': 'NONE'})  # replace NA with NONE

    toDict = df.to_dict('records')  # Convert back to dictionary
    dataFinal = [collections.OrderedDict(d) for d in toDict]  # convert into ordered dictionary

    print("\nCleaned sample data : \n{}".format(dataFinal[:2]))  # print cleaned head data

    return dataFinal  # returned data


def readFile(filename):
    """ This is a generic routine to read csv files using dictionary reader and return rows as dictionary items
    :param filename: File name with path for file read
    :return: list of dictionary of file records
    """
    csvFile = open(filename, 'r')  # Open input file
    dictReader = csv.DictReader(csvFile)  # setup dictionary reader
    return [d for d in dictReader]  # Convert each record into a dictionary list items & return


def writeFile(filename, rows, header):
    """ This is a generic routine to read csv files using dictionary reader and return rows as dictionary items
    :param filename: File name with path
    :param rows: data to be written
    :param header: header data found in input
    :return: no return data
    """
    csvFile = open(filename, 'w', newline="")  # Open in write mode

    new_rows = []  # Empty list
    for data_dict in rows:  # Loop through all data rows
        new_row = {}  # start with empty
        for key in header.keys():  # Loop through all header
            new_row[key] = data_dict[key]  # add column
        new_rows.append(new_row)  # Append selected headers

    dictWriter = csv.DictWriter(csvFile, header)  # Prepare dictionary writer
    dictWriter.writeheader()  # Go write header
    dictWriter.writerows(new_rows)  # GO write data


def getData():
    """ This routine reads input data and returns combined single dataset for analysis work
    :return: returns combined input data which is list of ordered dictionary
    """
    dataRows = readFile(input1)  # read the athlete data file
    nocRows = readFile(input2)  # pull records in python dictionary

    new_rows = []  # Empty list to get cleaned rows

    for data_dict in dataRows:  # Loop through all data rows
        new_row = data_dict  # new dictionary for each row
        for noc_dict in nocRows:  # Loop through all header rows
            if data_dict['NOC'] == noc_dict['NOC']:  # Look for matching row
                new_row['region'] = noc_dict['region']  # add region column
                new_row['notes'] = noc_dict['notes']  # add notes column
                break  # exit from loop
        new_rows.append(new_row)  # Append new cleaned data

    return new_rows  # Return combined input data


def main():
    """ This is the mainline routine for this script
    :return: no return
    """
    inputData = getData()  # Go get data for processing
    cleanedData = clearData(inputData)  # Go clean the data now
    filteredHdr = filterHeader(list(cleanedData[0].keys()))  # Go retrieve data using interesting fields
    writeFile(outputFile, cleanedData, filteredHdr)  # Go and write cleaned data which can be used for further analysis


if __name__ == '__main__':
    main()
