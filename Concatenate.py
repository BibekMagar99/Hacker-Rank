# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:38:26 2021

@author: bibek
"""

#python2 program
import numpy
N,M,P = map(int, raw_input().split(" "))
arr= []
for i in range(N):
    arr.append(map(int, raw_input().split(" ")))
A = numpy.array(arr)
arr_2 = []
for i in range(M):
    arr_2.append(map(int, raw_input().split(" ")))
B = numpy.array(arr_2)
print numpy.concatenate((A, B), axis = 0)

