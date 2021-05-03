# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:17:15 2021

@author: bibek
"""

#python2 Program
import numpy
N,M = map(int,(raw_input().split()))
A = []
for i in range(N):
    A.append((map(int,raw_input().split())))
B = numpy.array(A)


print numpy.transpose(B)
print B.flatten()
    