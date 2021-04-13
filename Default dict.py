# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:00:04 2021

@author: bibek
"""

from collections import defaultdict
#importing DefaultDict
A = defaultdict(list)
B = defaultdict(list)
#creating two default dictionaries
b = []
c = []
#two empty lists

n,m = list(map(int, input().split()))
#taking two inputs and mapping them into integers and then converting into list

for i in range (n):
    b.append(input())
#creating the list of user input alphabets

for i in range (m):
    c.append(input())
#creating the list of alphabets to check in the list

for i in c:
#take ith elememt in c
    e = []
#create an empty list e

    for j in range (len(b)):
#run loop for all the elements in b
        try:
            e.append((b.index(i,j,j+1))+1)
#checks the index of ith element of c in b shifting one character at a time because
#if not shifted by 1 it will only output the the first found index
 
        except:
            pass
#if there is no match of index it will produce an error.

    if not e :
        print("-1")
#if e is an empty list prints -1
    else:
        print(' '.join(map(str, e)))
#printing the elements of list in same line
#https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/#:~:text=Without%20using%20loops%3A%20*%20symbol%20is,sep%3D%E2%80%9D%2C%20%E2%80%9D%20respectively.