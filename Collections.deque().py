# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:17:35 2021

@author: bibek
"""
from collections import deque
deq = deque()

N = int(input())
for i in range (N):
    inp = input()
    temp = inp.split(" ")
    if temp[0] == "append":
        deq.append(temp[1])
    elif temp[0] == "popleft":
        deq.popleft()
    elif temp[0] == "appendleft":
        deq.appendleft(temp[1])
    else:
        deq.pop()
print(" ".join(map(str, deq)))