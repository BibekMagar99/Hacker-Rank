# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:59:39 2021

@author: bibek
"""

def average(array):
    return((sum(set(arr))/len(set(arr))))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)