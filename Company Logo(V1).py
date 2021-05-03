# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:18:16 2021

@author: bibek
"""
from collections import Counter
string = input()
for i in Counter(string).most_common(3):
    print(f"{i[0]} {i[1]}")


        
