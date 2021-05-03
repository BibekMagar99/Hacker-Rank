# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:00:22 2021

@author: bibek
"""
#for python2
import numpy

def arrays(arr):
    a = numpy.array(map(float,arr))
    return(a[::-1])
    

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)