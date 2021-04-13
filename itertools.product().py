# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:44:09 2021

@author: bibek
"""

from itertools import product
#importing product from itertools

a = map(int,input().split())
#taking multiple input in a single line and passing it to map function to convert into integer
b = map(int,input().split())

c = list(product(a,b))
#taking cartesian product
for i in c:
    print(i,end=" ")
#printing each element in a single line