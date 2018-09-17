# encoding: utf-8
'''
Created on 2018年9月17日

@author: Administrator
'''

import csv


filename = "files/sitka_weather_07-2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#     print(header_row)
    for index, header in enumerate(header_row):
        print(index, header)
