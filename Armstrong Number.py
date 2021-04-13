# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:42:45 2021

@author: bibek
"""

a = input()
cmp = list(map(int, list(a)))
som = 0
p = len(a)
for i in cmp:
    som = som+ i**p
if som == int(a):
    print("Armstrong")
else:
    print("not")

