# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:48:40 2021

@author: bibek
"""

import numpy
numpy.set_printoptions(legacy='1.13')
for i in range(3):
    A = numpy.array(list(map(float, input().split())))
    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))