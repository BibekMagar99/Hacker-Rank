# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:54:49 2021

@author: bibek
"""

N,X = map(int, input().split())
Z=[]
for i in range(X):
    A = list(map(float,input().split()))
    Z.append(A)
Scores = zip(*Z)
for i in Scores:
    print(sum(i)/len(i))