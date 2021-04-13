# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:41:40 2021

@author: bibek
"""

def print_rangoli(a):
    t = 96+a
    left = ""
    right = ""
    list_ok = []
    wid = a*4-3
    while (t != 97):
        middle = chr(t)
        #o = t-1
        print((left.rjust(0)+middle+right.ljust(0)).center(wid,"-"))
        list_ok.append((left.rjust(0)+middle+right.ljust(0)))
        l = chr(t)+"-"
        left = left + l
        r = "-"+chr(t)
        right = r + right
        t = t-1 
    print(left + "a" + right)       
    for i in list_ok[::-1]:
        print(i.center(wid,"-"))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)