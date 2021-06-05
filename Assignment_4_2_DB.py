# File:   Kumar_Shani_DSC540_Assignment_4_2_PDF.py
# Name:   Shani Kumar
# Date:   12/22/2019
# Course: DSC-540 - Data Preparation
# Desc:   Setup a local database with Python and load in a dataset (can be any dataset). You can choose what back-end
#         to use, if you have never done this before, the book recommends SQLite and to follow along with the book,
#         you can find that at: SQLite.
#           1. Create a Python dictionary of the data.
#           2. Create a new table.
#           3. Insert the data into that table.
# Usage:  This program is to complete assignment 4.2 requirements

import dataset

db = dataset.connect('sqlite:///collage.db')

student1 = {
    'name': 'Shani Kumar',
    'Address': 'Omaha Nebraska',
    'idnumber': '12345'
}

table = db['student_info']
table.insert(student1)

student2 = {
    'name': 'Rahul Suthar',
    'Address': 'Omaha Nebraska',
    'idnumber': '3456'
}

table.insert(student2)
sources = db['data_sources'].all()

print sources
