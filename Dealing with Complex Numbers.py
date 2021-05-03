# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:32:30 2021

@author: bibek
"""
import numpy
a ,b = map(int, input().split())
C = complex(a, b) 
a ,b = map(int, input().split())
D = complex(a, b) 
print(numpy.around((C+D),2))