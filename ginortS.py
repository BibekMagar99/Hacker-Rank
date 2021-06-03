# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:20:58 2021

@author: bibek
"""

string = input()
lower = []
upper = []
odd_digit = []
even_digit = []
for i in string:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isdigit:
        if int(i)%2==0:
            even_digit.append(i)
        else:
            odd_digit.append(i)
            
        
print("".join(sorted(lower))+"".join(sorted(upper))+"".join(sorted(odd_digit))+"".join(sorted(even_digit)))
