# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:33:34 2021

@author: bibek
"""
cube = lambda x: x**3

def fibonacci(n):
    a = n
    b = 0
    c = 1
    fib = []
    for i in range (a):
        fib.append(b)
        d = b + c
        b = c
        c = d
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

    