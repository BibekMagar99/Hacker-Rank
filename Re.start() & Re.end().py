# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:19:04 2021

@author: bibek
"""
import re
S = input()
k = input()

pattern = '(?={})'.format(re.escape(k))
m = list(re.finditer(pattern,S))

if m:
    for i in m:
        A = (i.start(),i.end()+len(k)-1)
        print(A)
else:
    print((-1,-1))

