# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:12:00 2021

@author: bibek
"""

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    k = int(input().strip())
    #print(arr)
    #https://stackoverflow.com/questions/16310015/what-does-this-mean-key-lambda-x-x1
    final = sorted(arr,key = lambda x : x[k])
    for i in final:
        print(" ".join([str(a) for a in i]))  
