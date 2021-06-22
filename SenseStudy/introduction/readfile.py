import urllib.request
import numpy as np
x = urllib.request.urlopen('https://raw.githubusercontent.com/yzhang0301/codes/master/SenseStudy/introduction/data.csv')
# raw data from the https link
str_raw = x.read().decode("UTF-8")
# split raw data to multiple strings ans stored as a list
str_list = str_raw.split('\r\n')
# split each row from a single string to multiple
total_row = len(str_list)
for row in range(total_row):
    str_list[row] = str_list[row].split(',')
print(str_list)
# erase the https heading from the first string element
str_list[0][0] = str_list[0][0].replace('\ufeff', '')
print(str_list)
# remove the last empty element caused by split function
str_list.pop()
print(str_list)
