# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 08:05:43 2021

@author: bibek
"""
from itertools import combinations
N = int(input())
elements = input().split()
K = int(input())
count = 0
total = len(list(combinations(elements,K)))
_combinations = combinations(elements,K)
for i in _combinations:
    if "a" in i:
        count = count+ 1
print(f"{(count/total):.3f}")

