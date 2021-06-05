# File:   Assignment_8_2_Selenium.py
# Name:   Shani Kumar
# Date:   02/03/2020
# Course: DSC-540 - Data Preparation
# Desc:   Web scraping with Selenium
#         Web scraping with Selenium  Follow along with your book starting on page 318-329 of Data Wrangling with
#         Python. At the end of the exercise, you should be able to go to a site, fill out a form, submit the form,
#         and then scroll through the results with the code you wrote. Make sure to submit the code and your output.
# Note:   This code uses Python 3.7 so it have code little be different then whats there in textbook.
# Usage:  This program is to complete assignment 8.2 requirements
#         Also web-page layout got changed to solution is little bit different from text book.
# Import required packages
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()    # setup web-browser
browser.get('http://google.com')  # set URL
inputs = browser.find_elements_by_css_selector('form input')  # find input field

for i in inputs:           # loop through inout
    if i.is_displayed():   # check whether displayed or not
        search_bar = i     # set search bar field
        break              # exit from loop

search_bar.send_keys('web scraping with python')   # send key for selected field
search_bar.submit()  # submit the page now

browser.implicitly_wait(10)  # wait for some time
results = browser.find_elements_by_css_selector('div.bkWMgd h2')  # select result

print(results)  # print result

for r in results:  # loop through result
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", r)
    action = webdriver.ActionChains(browser)  # setup field to formulate actions
    action.move_to_element(r)  # Ask browser to move to specified result
    action.perform()  # Now ask to perform the operation
    sleep(2)  # go to sleep for some time

browser.quit()  # close browser now
print("Done processing result page")  # print final message
