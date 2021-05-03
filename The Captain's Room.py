# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:14:07 2021

@author: bibek
"""
from collections import Counter
a = int(input())
b = Counter(input().split())
for i in b:
    if b[i]==1:
        print(i)
    else:
        pass
    
