# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 08:34:31 2021

@author: bibek
"""
import math
p = int(input())#AB
b = int(input())#BC

#pythagoras theorem h^2 = p^2 +b^2
h =(math.sqrt(p**2 + b**2))

MC = (1/2)*h

#area of triangle = (1/2)*base * height
area_ABC = (p*b)/2


#area of triangles standing on equal base and parallel lines are equal as the point B is same and AM = MC
area_BMC = area_ABC/2


#area_BMC = (1/2)*BM * BC * sin(theta)
#Also, BM = MC = AM 
#https://geometryhelp.net/right-triangles-median-to-hypotenuse-equals-half-the-hypotenuse/
BM = MC


#Answer in radian
theta = math.asin(area_BMC*2/(BM*b))

#conversion to degree and rounding
theta = round((theta * 180)/math.pi)

print(str(theta)+u"\u00b0")

#this didnot work
#press alt -> 2 -> 4 -> 8 to get the degree symbol
#print(str(theta)+"°")


#https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python