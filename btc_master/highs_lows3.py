# encoding: utf-8
'''
Created on 2018年9月17日

@author: Administrator
'''

import csv
from matplotlib import pyplot
from datetime import datetime


# filename = "files/sitka_weather_07-2014.csv"
filename = "files/sitka_weather_2014.csv"
filename = "files/death_valley_2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date, " missing data")
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
    
fig = pyplot.figure(dpi=128, figsize=(10, 6))

pyplot.plot(dates, highs, c="red", alpha=0.5)
pyplot.plot(dates, lows, c="blue", alpha=0.5)
pyplot.fill_between(dates, highs, lows, facecolor="blue", alpha=0.5)

# pyplot.title("Daily high temperatures,July 2014", fontsize=14)
title = "Daily high temperatures - 2014"
title = "Daily high temperatures - 2014\n Death Valley,CA"
pyplot.title("Daily high temperatures - 2014", fontsize=14)
pyplot.xlabel("", fontsize=16)
fig.autofmt_xdate()
pyplot.ylabel("Tempaure (F)", fontsize=16)

pyplot.tick_params(axis="both", which="major", labelsize=16)
pyplot.show()
