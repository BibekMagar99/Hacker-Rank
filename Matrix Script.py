# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:07:12 2021

@author: bibek
"""

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
final_word = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for element in matrix:
        final_word.append(element[i])
sentence = "".join(final_word)

print(re.sub(r'(?<=\w)+([^\w]+)(?=\w)+', ' ', sentence))
        
        
