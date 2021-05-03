# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:02:00 2021

@author: bibek
"""

import numpy
N,M = map(int, raw_input().split(" "))
A = []
for i in range (N):
    A.append(map(int, raw_input().split(" ")))
A = numpy.array(A)
B = []
for i in range (N):
    B.append(map(int, raw_input().split(" ")))
B = numpy.array(B)
print numpy.add(A, B)
print numpy.subtract(A, B)
print numpy.multiply(A, B)
print numpy.divide(A, B)
print numpy.mod(A, B)
print numpy.power(A, B)