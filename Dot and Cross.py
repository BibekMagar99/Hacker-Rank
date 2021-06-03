# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:40:39 2021

@author: bibek
"""

import numpy
N = int(input())
A=[]
B=[]
C=[]
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
A = numpy.array(A)
for i in range(N):
    a = list(map(int, input().split()))
    B.append(a)
B = numpy.array(B)
print(numpy.dot(A,B))
    