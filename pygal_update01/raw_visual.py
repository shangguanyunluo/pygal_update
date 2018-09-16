# encoding: utf-8
'''
Created on 2018年9月16日

@author: Administrator
'''

from matplotlib import pyplot

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    pyplot.scatter(rw.x_values, rw.y_values, s=15)
    
    pyplot.show()
    
    keep_running = input("Make anotherwalk?(y/n)")
    if keep_running == "n":
        break