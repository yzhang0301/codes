import urllib.request
import numpy as np
x = urllib.request.urlopen('https://raw.githubusercontent.com/yzhang0301/codes/master/SenseStudy/introduction/data.txt')
str_list=x.read().decode("UTF-8").split('\r\n')
print(str_list)
