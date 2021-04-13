# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:58:47 2021

@author: bibek
"""

from itertools import permutations
#importing the libraries

ok,no = input().split()
#taking two inputs, i.e string and the number like HACK and  2

r = int(no)
#converting the number into integer

result = sorted(permutations(ok,r))
#sorting the list achieved from the permutations of the string 

for i in result:
#taking each element and joining them without space and printing them
    print("".join(i))