# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:35:33 2021

@author: bibek
"""


n = int(input())
_n = set(input().split())
b = int(input())
_b = set(input().split())
print(len(_n.symmetric_difference(_b)))
