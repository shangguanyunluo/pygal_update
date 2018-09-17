# encoding: utf-8
'''
Created on 2018年9月17日

@author: Administrator
'''

import csv
from matplotlib import pyplot


filename = "files/sitka_weather_07-2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
    
fig = pyplot.figure(dpi=128, figsize=(10, 6))
pyplot.plot(highs, c="red")

pyplot.title("Daily high temperatures,July 2014", fontsize=14)
pyplot.xlabel("", fontsize=16)
pyplot.ylabel("Tempaure (F)", fontsize=16)

pyplot.tick_params(axis="both", which="major", labelsize=16)
pyplot.show()
