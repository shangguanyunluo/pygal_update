# encoding: utf-8
'''
Created on 2018年9月13日

@author: Administrator
'''

from matplotlib import pyplot

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

pyplot.scatter(x_values, y_values)

pyplot.title("Squares Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

pyplot.tick_params(axis="both", which="major", labelsize=14)

pyplot.show()
