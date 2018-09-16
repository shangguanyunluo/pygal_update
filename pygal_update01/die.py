# encoding: utf-8
'''
Created on 2018年9月16日

@author: Administrator
'''

from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, self.num_sides)
