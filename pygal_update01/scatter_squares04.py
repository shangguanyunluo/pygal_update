# encoding: utf-8
'''
Created on 2018年9月13日

@author: Administrator
'''
from matplotlib import pyplot

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

pyplot.scatter(x_values, y_values, c="red", edgecolors="none", s=40)

pyplot.title("Squares Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

pyplot.axis([0, 1100, 0, 1100000])

pyplot.show()
