# encoding: utf-8
'''
Created on 2018年9月16日

@author: Administrator
'''
from die import Die
import pygal

die = Die()

results = []
for roll in range(1000):
    results.append(die.roll())
    
frequencies = []
for num in range(1, die.num_sides + 1):
    frequencies.append(results.count(num))
print(frequencies)

hist = pygal.Bar()

hist.title="Results of rolling on 6D 1000 times"
hist.x_title="Results"
hist.y_title="Frequencies of Results"

hist.add("D6", frequencies)
hist.render_to_file("die.visual.svg")
hist.render_to_file("die.visual.png")
