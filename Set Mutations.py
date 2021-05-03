# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:40:56 2021

@author: bibek
"""

A = int(input())
A_elements = set(input().split())
N = int(input())
for i in range(N):
    execution, n = input().split()
    n = int(n)
    elements = set(input().split())
    if execution=='intersection_update':
        A_elements.intersection_update(elements)
    elif execution=='update':
        A_elements.update(elements)
    elif execution=='symmetric_difference_update':
        A_elements.symmetric_difference_update(elements)
    elif execution=='difference_update':
        A_elements.difference_update(elements)
A_elements = map(int, A_elements)
print(sum(A_elements))
