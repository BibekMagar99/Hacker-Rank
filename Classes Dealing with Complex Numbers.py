# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:42:23 2021

@author: bibek
"""

a,b = map(float,(input().split()))
C = complex(a,b)
a,b = map(float,(input().split()))
D = round(complex(a,b),2)
print(C+D)