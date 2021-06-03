# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:58:37 2021

@author: bibek
"""

"""  THIS ALMOST WORKED 
N = int(input())
lines = ""
for i in range(N):
    lines+=input()+"\n"
line = lines.replace(" && ", " and ")
line = line.replace(" || ", " or ")
print(line)

this did not work because it only replaced one occurence of the pattern.



import re
N = int(input())
line = ""
for i in range(N):
    line = line + input() +"\n"
line = re.sub(r"\s\|\|\s"," or ", line)
line = re.sub(r"\s\&\&\s"," and ", line)
print(line)

BOTH HAD THE SAME PROBLEM

x&& &&& && && x || | ||\|| x
could not replace the second && with and
"""

#finally this worked by using a while loop
import re
N = int(input())
line = ""
for i in range(N):
    line = line + input() +"\n"
while (' && ' in line) or (' || ' in line):
    line = re.sub(r"\s\|\|\s"," or ", line)
    line = re.sub(r"\s\&\&\s"," and ", line)
print(line)