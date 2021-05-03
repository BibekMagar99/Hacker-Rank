# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:07:02 2021

@author: bibek
"""

#python2
import numpy
N,M = map(int, raw_input().split(" "))
A = []
for i in range (N):
    A.append(map(int, raw_input().split(" ")))
A = numpy.array(A)
print numpy.mean(A, axis = 1)
print numpy.var(A, axis = 0)
print round(numpy.std(A, axis = None),11)