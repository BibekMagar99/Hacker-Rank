# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:40:49 2021

@author: bibek
"""

def print_formatted(number):
    '''Prints number in decinmal, ocal, hexadecimal, and binary'''
    for i in range(1, number + 1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)