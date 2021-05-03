# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:34:19 2021

@author: bibek
"""
from itertools import groupby
string = input()
group = [list(g) for k, g in groupby(string)]
for i in group:
    a =(len(i),int(i[0]))
    print(a,end = " ")

#https://docs.python.org/2/library/itertools.html#itertools.groupby