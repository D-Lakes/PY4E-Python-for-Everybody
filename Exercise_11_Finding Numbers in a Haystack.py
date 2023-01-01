#  Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment
#   Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#   Actual data: http://py4e-data.dr-chuck.net/regex_sum_1710453.txt (There are 56 values and the sum ends with 62)

import re
# Create File Handle to access files
file_name = input('Enter File Name: ')
if len(file_name) < 1:
    file_name = 'regex_sum_1710453.txt'
elif file_name == '1':
    file_name = 'regex_sum_42.txt'
f_handle = (open(file_name))

# Create variables to be used in data manipulation
numbers = list()
data = f_handle.read()

# Parse through file and extract all numbers into a list
numbers = re.findall('[0-9]+', data)

# Test to see if the correct amount of numbers were extracted:
# print(len(numbers))

# Convert list of numbers from type str to type int and print their sum
print('Sum of numbers in file:',sum([int(number) for number in numbers]))

#Full List Comprehension version. Was confused why it kept returning 0 until I read the official documentation for the .read() method
f_handle.seek(0)
print(sum([int(x) for x in re.findall('[0-9]+',f_handle.read())]))


