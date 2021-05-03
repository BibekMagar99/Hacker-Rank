# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:08:42 2021

@author: bibek
"""

#python2

import numpy
N,M = map(int, raw_input().split(" "))
A = []
for i in range (N):
    A.append(map(int, raw_input().split(" ")))
A = numpy.array(A)
sum_arr = numpy.sum(A, axis = 0)
print numpy.prod(sum_arr)   