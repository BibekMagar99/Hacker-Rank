# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:11:05 2021

@author: bibek
"""

import re
N = int(input())
for i in range(N):
    number = input()
    try:
        a = int(number)
        
        if len(number)==10:
            if re.match(r'^[987]',number):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    except:
        print("NO")