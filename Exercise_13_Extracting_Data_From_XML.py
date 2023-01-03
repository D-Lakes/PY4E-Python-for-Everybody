# Extracting Data from XML
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1710457.xml (Sum ends with 58)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#Enter url address
url = input('Enter location: ')
if url == '1':
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
if url == '2':
        url = 'http://py4e-data.dr-chuck.net/comments_1710457.xml'
# Obtain XML Object, Store into variable as a string, and decode
xml_request = urllib.request.urlopen(url)
data = xml_request.read()
print(data.decode())
# Pard through string, create list with all comment tags, extract the number in each tag and append toa  list and print their sum
tree = ET.fromstring(data)
counts = tree.findall('.//count')
numbers = list()
for count in counts:
    numbers.append(count.text)
print(sum([int(x) for x in numbers]))



