# encoding: utf-8
'''
Created on 2018年9月16日

@author: Administrator
'''

from matplotlib import pyplot

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    pyplot.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=pyplot.cm.Blues)
    
    pyplot.scatter(0, 0, c="green", edgecolors="none", s=100)
    pyplot.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
#     pyplot.scatter(rw.x_values, rw.y_values, s=15)
    
    pyplot.axes().get_xaxis().set_visible(False)
    pyplot.axes().get_yaxis().set_visible(False)
    
    pyplot.show()
    
    keep_running = input("Make anotherwalk?(y/n)")
    if keep_running == "n":
        break
