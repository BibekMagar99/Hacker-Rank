# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:53:19 2021

@author: bibek
"""

from collections import Counter
#importing Counter

x = int(input())
#taking integer input for no of shoes

sizes = map(int, input().split())
#taking multiple inputs and converting them into integer

dictionary = Counter(sizes)
#converting the sizes into dictionary where each object is counted

number = int(input())
#how many required

total = 0
for i in range(number):
#iterating the loop as per the user need
    
    (reqd_size,price) =map(int, input().split())
#taking two inputs customer need and price
    
    if dictionary[reqd_size]>0:
#if the required size has appeared at least one time in the dictionary of the size list i.e its count is 1
        dictionary[reqd_size] = dictionary[reqd_size]-1
#decrease the count by 1(because it can be repeated more than once
        
        total = total+price

print(total)