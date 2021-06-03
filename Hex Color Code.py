# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:45:38 2021

@author: bibek
"""

import re
n= int(input())
for i in range(n):
    a = input()
    match=re.findall(r"(\#[a-fA-F0-9]{3,6})[\;\,\)]{1}",a)
    if match:
        for i in list(match):
            print(i)
