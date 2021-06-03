# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:29:41 2021

@author: bibek
"""
#question says return true if:
#1. All the integers separated by space are positive
#2. If any of the space separated numbers is a palindrome
a =int(input())
nums = list(map(int, input().split()))
print(all(i>0 for i in nums) and any(str(a) == str(a)[::-1] for a in nums))
