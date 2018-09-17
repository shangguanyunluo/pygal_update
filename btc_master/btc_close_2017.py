# encoding: utf-8
'''
Created on 2018年9月17日

@author: Administrator
'''
# from __future__ import (absolute_import, division, print_function, unicode_literals)

import json, math

filename = "files/btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, close = [], [], [], [], []   
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(btc_dict['month'])
    weeks.append(btc_dict['week'])
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
#     print("{} is month {} week {},{},the close price is {} RMB".format(date, month, week, weekday, close))

import pygal

line_chart = pygal.Line(x_label_rotation=20, show_monitor_x_labels=False)
line_chart.title = "收盘价（￥）"
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add("收盘价", close_log)
# line_chart.render_to_file("收盘价折线图（￥）.svg")
line_chart.render_to_file("收盘价对数变换折线图（￥）.svg")
