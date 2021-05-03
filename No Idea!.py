# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:54:53 2021

@author: bibek
"""
def happines_add():
    happiness = 0
    for i in range(len(Array)):
        if Array[i] in A:
            happiness += 1
    return happiness

def sad():
    happiness = 0
    for i in range(len(Array)):
        if Array[i] in B:
            happiness -= 1
    return happiness
    
        

n,m = map(int,input().split())
Array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
A_count = happines_add()
B_count = sad()
final = A_count + B_count
print(final)

