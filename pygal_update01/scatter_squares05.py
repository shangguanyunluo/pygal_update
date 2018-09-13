# encoding: utf-8
'''
Created on 2018年9月13日

@author: Administrator
'''

from matplotlib import pyplot

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

pyplot.scatter(x_values, y_values, c=y_values, edgecolors="none", s=40, cmap=pyplot.cm.Blues)

pyplot.title("Square Numbers", fontsize=14)
pyplot.xlabel("Value")
pyplot.ylabel("Squares of Numbers")

pyplot.axis([0, 1100, 0, 1100000])
# pyplot.show()
pyplot.savefig("squares_ploy.png",bbox_inches="tight")
