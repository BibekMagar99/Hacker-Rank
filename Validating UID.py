# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:56:13 2021

@author: bibek
"""

import re
N = int(input())
for i in range(N):
    ID = "".join(sorted(input()))
    if len(set(ID))==10 and ID.isalnum(): 
        if bool(re.search(r"[A-Z]{2,}",ID) and re.search(r"\d{3,}",ID)):
            print("Valid")
        else:
            print("Invalid")  
    else:
        print("Invalid")