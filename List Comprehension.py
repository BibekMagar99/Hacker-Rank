# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:43:32 2021

@author: bibek
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ok = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
    final = [i for i in ok if sum(i)!=n]
    print(final)