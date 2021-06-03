# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:38:35 2021

@author: bibek
"""

import numpy
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
print(numpy.inner(A, B))
print(numpy.outer(A, B))