# encoding: utf-8
'''
Created on 2018年9月13日

@author: Administrator
'''

from matplotlib import pyplot

pyplot.scatter(2, 4)

pyplot.title("Squares Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

pyplot.tick_params(axis="both", which="major", labelsize=14)

pyplot.show()
