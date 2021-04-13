# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:28:37 2021

@author: bibek
"""
#importing weque because it can access the eleents from right and left
from collections import deque

n = int(input())
for i in range (n):
    N = int(input())
    inp = deque(map(int, input().split()))
    
    #to compare the elements
    cmp = max(inp[0],inp[-1])
    for i in range(N):
        #if cmp is greater than left and right only then smaller can stay on top else not
        if cmp>=inp[0] and cmp>=inp[-1]:
            if inp[0] >= inp[-1]:
                inp.popleft()
            elif inp[0] < inp[-1]:
                inp.pop()
        else:
            break
        
    if len(inp)==0:
        print("Yes")
    else:
        print("No")
                
        

