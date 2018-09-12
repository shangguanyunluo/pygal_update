# encoding: utf-8
'''
Created on 2018年9月12日

@author: Administrator
'''

from matplotlib import pyplot

squares = [1, 4, 9, 16, 25]

pyplot.plot(squares, linewidth=5)

pyplot.title("Squares Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

pyplot.tick_params(axis="both", labelsize=14)
pyplot.show()
