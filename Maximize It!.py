# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:20:21 2021

@author: bibek
"""
from itertools import product
K,M = map(int,(input().split()))
S = 0
L = []
for i in range(K):
    A = list(map(int, input().split()))
    L.append(A[1:])
#print(L)
prod = list(product(*L))
#print(prod)
for i in prod:
    value = 0
    for a in i:
        value = value +int(a)**2
    #print(value)
    if (value%M) > S:
        S = value%M
    else:
        pass
   # print(S)
print(S)
