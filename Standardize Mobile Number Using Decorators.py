# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:16:37 2021

@author: bibek
"""

def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
