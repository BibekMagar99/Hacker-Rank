# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:21:15 2021

@author: bibek
"""
import re
N = int(input())
for i in range(N):
    card = input()
    case1 = re.match(r"[456][0-9]{15}",card)
    case2 = re.match(r"[456]\d{3}\-\d{4}\-\d{4}\-\d{4}",card)
    
    
https://github.com/rene-d/hackerrank/blob/master/python/py-regex/validating-credit-card-number.py