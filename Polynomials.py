# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:44:56 2021

@author: bibek
"""

import numpy
a = list(map(float, input().split()))
b = int(input())
print(numpy.polyval(a, b))