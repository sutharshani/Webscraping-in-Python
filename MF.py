# File:   MF.py
# Name:   Shani Kumar
# Date:   02/29/2020
# Course: DSC-540 - Data Preparation
# Desc:   Web scraping with Selenium & BeautifulSoup
#         This program will web scrape moneycontrol website to retrieve top equity mutual fund performance data.
#         It goes through various kind of equity fund pages to put there im a single excel spreadsheet.
#
# Usage:  This program is to complete assignment 12.3 requirements
#
# Import required packages
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import xlsxwriter

url = 'https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/large-cap-fund.html'  # Base URL
outputFile = 'Mutual Fund (Equity) Performance Data.xlsx'
# start with empty data
myHeader = []
myData = []
FullData = []


def remove_suffix(str1, suffix):
    """ This routine looks for specific suffix and return the string after removing that suffix.
    :param str1: Full string where it looks in for suffix
    :param suffix: Prefix string that it want to remove
    :return: string without suffix
    """
    strData = str1
    for elm in suffix:
        if strData.endswith(elm):  # Check if it starts with specified suffix
            strData = strData[:len(strData)-len(elm)]  # return string without the specified string
    return strData


def remove_prefix(str1, prefix):
    """ This routine looks for specific prefix and return the string after removing that prefix.
    :param str1: Full string where it looks in for prefix
    :param prefix: Prefix string that it want to remove
    :return: string without prefix
    """
    if str1.startswith(prefix):  # Check if it starts with specified prefix
        return str1[len(prefix):]  # return string without the specified string
    else:
        return str1  # return string as it dont have matching string


def GetHeader(soup):
    """  This routine looks in the soup and search the header data.
    :param soup: Input soup data
    :return: header data
    """
    header = []  # start with empty header fields
    for data1 in soup.find_all('th', attrs={'aria-controls': 'dataTableId'}):  # loop through header fields
        header.append(data1.text.rstrip())  # append header data
    return header  # return header data


def GetData(soup):
    """ This routine sets up log file and configure logging setting.
    :return: no return from this routine
    """
    tbody = soup.find_all('tbody')
    for data1 in tbody[1].find_all('tr'):
        row = []
        for data2 in data1.find_all('td'):
            row.append(remove_prefix(data2.text.rstrip().strip("%"), "Sponsored AdvInvest Now"))
        myData.append(row)


def browseAndFetchData(myUrl):
    """ This routine browse the url provided and fetch all the data required.
    :param myUrl: input URL string
    :return: no return data
    """
    browser = webdriver.Firefox()  # setup web-browser
    browser.get(myUrl)  # set URL
    elements = browser.find_elements_by_css_selector('li[data-invtype="Equity"]')  # find Equity buttons

    for index in range(len(elements)):  # loop through for all the buttons len(elements)
        elements = browser.find_elements_by_css_selector('li[data-invtype="Equity"]')  # find Equity field
        elements[index].click()  # click button
        element = browser.find_element_by_css_selector('input[id="directPlan"]')  # find Equity field
        element.click()  # click button

        soup_level1 = BeautifulSoup(browser.page_source, 'html.parser')  # hand the page source to Beautiful Soup
        if index == 0:  # Get header only once
            global myHeader  # access global field
            myHeader = GetHeader(soup_level1)
        GetData(soup_level1)
        sleep(1)
    browser.quit()  # close browser now


def cleanFundName(name):
    """ This routine cleans Fund Name
    :param name: input find data
    :return: return clean name
    """
    suffix = ['Large Cap Fund', 'Multi Cap Fund', 'Large & Mid Cap Fund', 'Mid Cap Fund', 'Small Cap Fund', 'ELSS',
              'Dividend Yield Fund', 'Sectoral/Thematic', 'Contra Fund', 'Focused Fund', 'Value Fund', 'RGESS']
    cleanName = remove_suffix(name, suffix)
    return cleanName


def cleanData(inputData):
    """ This routine clean the input data
    :param inputData: input fund performance data
    :return: returns clean data
    """
    cleandata = []  # start with empty data
    for data in inputData: # loop through all data
        row = []  # start with empty row
        if not (data[2].startswith('Direct Plan') or data[2].startswith('Regular')):  # remove bad category name
            for indx, value in enumerate(data): # loop through row
                if indx == 0:  # check for fund name
                    val = cleanFundName(value)  # clean fund name
                elif len(value) == 1:  # clean one byte data field
                    val = value.strip('-')  # clean '-'
                    if val == '':  # check for empty data
                        val = 0  # init to zero
                else:  # otherwise
                    if indx > 4:  # look for performance figures
                        val = float(value)  # convert to float
                    else:
                        val = value  # just copy otherwise
                row.append(val)  # append to row data
            cleandata.append(row)  # append to data
    return cleandata  # return data


def cleanHeader(hdr):
    """ This routine clean the input data
    :param hdr: input header data
    :return: returns clean data
    """
    cleanHdr = []  # start with empty header
    for idx, value in enumerate(hdr):  # loop through header
        if idx > 4:  # loop for performance headers
            val = value + " (%)"  # add % to header
        else:
            val = value  # otherwise just copy
        cleanHdr.append(val)  # append header data
    return cleanHdr  # return header data


def combineData(header, perfData):
    """ This routine combines data provided in argument
    :param header: header data
    :param perfData: performance data
    :return: returns combined data
    """
    combinedData = [header]
    for data in perfData:  # loop through all data rows
        combinedData.append(data)  # append row data
    return combinedData  # return combined data


def writeData(data):
    """ This routine writes data in excel spreadsheet
    :param data: web scrapped data
    :return: no return
    """
    workbook = xlsxwriter.Workbook(outputFile)
    worksheet = workbook.add_worksheet('Top Performing Equity MF')
    for row_num, row in enumerate(data):
        for col_num, col in enumerate(row):
            worksheet.write(row_num, col_num, col)
    workbook.close()
    print("Data writen into spreadsheet")


def main():
    """ Script mainline routine
    :return: no return data
    """
    global myData, myHeader, FullData
    browseAndFetchData(url)  # go browse the data and fetch in our python script
    myData = cleanData(myData)  # go clean the data
    myHeader = cleanHeader(myHeader)  # go clean the header data now
    FullData = combineData(myHeader, myData)  # Combine header and fund performance data

    print("Titles of web scrapped data: \n{}\n".format(myHeader))  # print header data
    print("Total Records: {}\nNumber of data variables: {}\n".format(len(myData),len(myHeader)))  # print details
    writeData(FullData)  # go write data now


# Start here
if __name__ == '__main__':
    main()
