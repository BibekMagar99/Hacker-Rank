# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:14:29 2021

@author: bibek
"""

num_Eng = int(input())
#taking space-separated values and converting into sets
roll_num = set(input().split())
num_Fre = int(input())
roll_nums = set(input().split())

# | = union
print(len(roll_num | roll_nums))
#OR
#print(len(roll_num.union(roll_nums)))

