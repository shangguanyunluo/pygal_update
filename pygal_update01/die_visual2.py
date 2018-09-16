# encoding: utf-8
'''
Created on 2018年9月16日

@author: Administrator
'''
from die import Die
import pygal

die1 = Die()
die2 = Die(10)

results = []
for roll in range(5000):
    result = die1.roll() + die2.roll()
    results.append(result)
    
frequencies = []
max_num = die1.num_sides + die2.num_sides
for num in range(2, max_num + 1):
    frequencies.append(results.count(num))
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling a 6D and a d10 1000 times"
hist.x_labels = [x for x in range(2, max_num + 1)]
hist.x_title = "Results"
hist.y_title = "Frequencies of Results"

hist.add("D6+D10", frequencies)
hist.render_to_file("die.visual.svg")
