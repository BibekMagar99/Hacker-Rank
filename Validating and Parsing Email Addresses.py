# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:21:36 2021

@author: bibek
"""
import re
n = int(input())
emails = [input() for i in range(n)]
for i in emails:
    A = i.split(" ")
    if (re.match("^\<([a-z])([a-zA-Z0-9\-\.\_])+\@([a-zA-Z])+\.([a-zA-Z]){1,3}\>$",A[1])):
        print(A[0], A[1])