# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:07:02 2021

@author: bibek
"""
import numpy
N, M = list(map(int,(input().split())))
arr = []
for i in range (N):
    a = list(map(int, input().split()))
    arr.append(a)
final_array = numpy.array(arr)
max_axis = numpy.min(final_array,axis = 1)
print(numpy.max(max_axis))
    