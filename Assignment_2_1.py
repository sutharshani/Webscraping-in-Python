# File:   Kumar_Shani_DSC540_Assignment2_2.py
# Name:   Shani Kumar
# Date:   12/08/2019
# Course: DSC-510 - Data Preparation
# Desc:   01. Change case in a string
#         02. Strip space off the end of a string
#         03. Split a string
#         04. Add and Subtract integers and decimals
#         05. Create a list
#         06. Add to the list
#         07. Subtract from the list
#         08. Remove the last item from the list
#         09. Re-order the list
#         10. Sort the list
#         11. Create a dictionary
#         12. Add a key-value to the dictionary
#         13. Set a new value to corresponding key in dictionary
#         14. Look a new value by the key in dictionary
# Usage:  This program is to complete assignment 2.1 requirements
# Needed to use raw_input function instead of input function. input function gives namError when used in MacOS.

# Change case in a string
Str1 = "My Dummy string"
print("String before any case conversion: '{}'".format(Str1))
print("String after upper case conversion: '{}'".format(Str1.upper()))
print("String after lower case conversion: '{}'".format(Str1.lower()))

# Strip space off the end of a string
str2 = "My Dummy string with spaces after it         "
print("String before stripping spaces: '{}'".format(str2))
print("String after stripping spaces: '{}'".format(str2.strip()))

# Split a string
print("String split using space: {}; Type = {}".format(str2.strip().split(" "), str2.strip().split(" ").__class__))

# Add and Subtract integers and decimals
print("Integer Addition: (4 + 5) = {}".format(4 + 5))
print("Integer Subtraction: (6 -3) = {}".format(6 - 3))
print("Decimal Addition: (5.4 + 3.5) = {}".format(5.4 + 3.5))
print("Decimal Subtraction: (5.4 - 3.5) = {}".format(5.4 - 3.5))

# Create a list
list1 = ['Shani']
print("Initial test list: {}".format(list1))

# Add to the list
list1.append('Suthar')
list1.append('Kumar')
list1.append('lal')
print("List after adding items: {}".format(list1))

# Subtract from the list
list1.pop(1)
print("List after removing an item from index 1 using pop: {}".format(list1))

# Remove the last item from the list
del list1[-1]
print("List after removing an last item: {}".format(list1))

# Re-order the list
orderlist = [1, 0]
print("List {} reordered based on order {} to form "
      "new list: {}".format(list1, orderlist, [list1[i] for i in orderlist]))

# Sort the list
list2 = [3, 4, 6, 2, 1, 0]
print("List before sorting: {}".format(list2))
list2.sort()
print("List after sorting:{}".format(list2))

# Create a dictionary
student = {'name': 'Shani Kumar'}
print("Initial Dictionary: {}".format(student))

# Add a key-value to the dictionary
student['class'] = "DSC-540"
student['city'] = "Omaha"
print("Dictionary after adding  values: {}".format(student))

# Set a new value to corresponding key in dictionary
student['class'] = "DSC140 - Data Preparation"
print("Dictionary after changing class value: {}".format(student))

# Task 14: Look a new value by the key in dictionary
print("Dictionary - value by key 'class' : {}".format(student.get("class")))