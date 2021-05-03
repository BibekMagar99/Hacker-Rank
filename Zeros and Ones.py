# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:44:44 2021

@author: bibek
"""
#python2 program
import numpy
tup = tuple(map(int, (raw_input().split(" "))))
print numpy.zeros((tup), dtype = numpy.int)
print numpy.ones((tup), dtype = numpy.int)