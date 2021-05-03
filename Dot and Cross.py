# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:13:31 2021

@author: bibek
"""


#python2 Program
import numpy
N = map(int, raw_input())
A = []
B = []
for i in range(N):
    for i in range(N):
        A.append((map(int,raw_input().split())))
    A = numpy.array(A)