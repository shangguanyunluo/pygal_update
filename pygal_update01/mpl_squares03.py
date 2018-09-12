# encoding: utf-8
'''
Created on 2018年9月13日

@author: Administrator
'''

from matplotlib import pyplot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

pyplot.plot(input_values, squares, linewidth=4)

pyplot.title("Square Numbers",fontsize=20)
pyplot.xlabel("Value")
pyplot.ylabel("Square of Numbers")

pyplot.tick_params(axis="both")
pyplot.show()
