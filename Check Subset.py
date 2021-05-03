# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:48:40 2021

@author: bibek
"""

T = int(input())
for i in range(T):
    A = int(input())
    A_elements = set(input().split())
    B = int(input())
    B_elements = set(input().split())
    print(A_elements.issubset(B_elements))
