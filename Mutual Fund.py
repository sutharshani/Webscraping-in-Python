# File:   Assignment_8_2_Beautiful_Soup.py
# Name:   Shani Kumar
# Date:   02/03/2020
# Course: DSC-540 - Data Preparation
# Desc:   Beautiful Soup –
#         Reading a Web Page with Beautiful Soup – following the example starting on page 300-304 of
#         Data Wrangling with Python, use the Beautiful Soup Python library to scrap a web page.
#         The result should be data and output in an organized format. Each of the data entries should be in its
#         own dictionary with matching keys.
# Note:   This code uses Python 3.7 so it have code little be different then whats there in textbook.
# Usage:  This program is to complete assignment 8.2 requirements
#         Also web-page layout got changed to solution is little bit different from text book.
# Import required packages
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.moneycontrol.com/mutual-funds/find-fund/returns?&amc=BIRMUTF,AXMF,BOBMUF,ABNAMF,'
                    'BAXMF,CANMUTF,DSPMLMF,EDELWMF,PEERMF,TEMMUFT,HDFCMUTF,HSBCMUTF,PRUICM,IDBIMF,ANZGRMUTF,IDFMF,'
                    'IIFLMF,ILFSMF,INDIABMF,LIMF,ITIMF,JMMTFN,KMFLAMC,CHCAMUF,LICAMCL,MAHMF,MIRAEMF,MOMF,RELCAPM,PMF'
                    ',PPFMF,IDBIMUT,ESCOMUF,QMF,FIINMUFD,SBIMUTF,SHMF,SUNMUTF,TATMUTF,TAUMUTF,UKBCMF,UTIMUTFD,YESMF&'
                    'invtype=Equity%2CHybrid%2CDebt%2CSolution%20Oriented%2COthers&category=Multi%20Cap%20Fund,'
                    'Large%20Cap%20Fund,Large%20%26%20Mid%20Cap%20Fund,Mid%20Cap%20Fund,Small%20Cap%20Fund,ELSS,'
                    'Dividend%20Yield%20Fund,Sectoral%2FThematic,Contra%20Fund,Focused%20Fund,Value%20Fund,RGESS,'
                    'Aggressive%20Hybrid%20Fund,Conservative%20Hybrid%20Fund,Arbitrage%20Fund,Capital%20Protection'
                    '%20Funds,Equity%20Savings,Dynamic%20Asset%20Allocation%20or%20Balanced%20Advantage,Multi%20Asset'
                    '%20Allocation,Fixed%20Maturity%20Plans%20-%20Hybrid,Low%20Duration%20Fund,Short%20Duration%20'
                    'Fund,Medium%20Duration%20Fund,Medium%20to%20Long%20Duration%20Fund,Long%20Duration%20Fund,'
                    'Dynamic%20Bond%20Fund,Gilt%20Fund,Gilt%20Fund%20with%2010%20year%20constant%20duration,'
                    'Corporate%20Bond%20Fund,Credit%20Risk%20Fund,Floater%20Fund,Banking%20and%20PSU%20Fund'
                    ',Fixed%20Maturity%20Plans%20-%20Debt,Interval%20Plans,Ultra%20Short%20Duration%20Fund,Liquid%2'
                    '0Fund,Money%20Market%20Fund,Overnight%20Fund,Childrens%20Fund,Retirement%20Fund,Investment%20cum%'
                    '20Insurance,Fund%20of%20Funds,Index%20Funds%2FETFs&rank=1,2&MATURITY_TYPE=OPEN%20ENDED&SHOWAUM='
                    'Y&ASSETSIZE=100')   # setup url get request

# print(page.content)
bs = BeautifulSoup(page.content, 'html.parser')  # Start parsing with BS
ta_divs = bs.find_all("div", class_="wpb_text_column wpb_content_element")  # list to div required

# Initialize required fields
all_data = []
index = 1

for header in bs.find_all('h6'):  # loop through all headers
    data_dict = {'title': header.text,   # setup title text
                 'link': header.a.get('href'),  # setup title url
                 'about': ta_divs[index].find_next('p').get_text()} # setup title description
    all_data.append(data_dict)  # Append to dictionary
    index += 1

for dict in all_data:  # loop through all element
    print(dict)  # print data

