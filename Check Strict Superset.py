# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:58:41 2021

@author: bibek
"""

A = set(input().split())
N = int(input())
for i in range(N):
    check = set(input().split())
    if not A.issuperset(check):
        print(False)
        break
else:
    print(True)