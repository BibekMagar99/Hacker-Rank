# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:18:23 2021

@author: bibek
"""
#importing ordered dict
from collections import OrderedDict

#taking the int integer for looping n words
n = int(input())

#declaring ordered dictionary
d = OrderedDict()


for i in range(n):
    a = input()

#if the word is in the key of dictionary then increase the value by 1 else set it to 1    
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
#printing total no of keys in dictionary        
print(len(d))

#this can be done to print the values(1)
#taking all the values of the dictionary, passing it to string and joining them with space
#print(" ".join(map(str, d.values())))


#Or this can also be done (2) to print all the values
for i in d:
    print(d[i], end = " ")
        
    