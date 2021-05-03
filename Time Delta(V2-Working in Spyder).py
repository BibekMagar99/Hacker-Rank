
"""
Created on Thu Apr 15 16:33:35 2021

@author: bibek
"""

import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    #converting the given time into a date-time object
    time1 = dt.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time2 = dt.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    #converting into seconds
    sec1 = time1.timestamp()
    sec2 = time2.timestamp()
    
    if sec1>sec2:
        total = sec1-sec2
    elif sec1 == sec2:
        total = 0
    else:
        total = sec2-sec1
    print(int(total))


t = int(input())

for t_itr in range(t):
    t1 = input()
    t2 = input()
    time_delta(t1, t2)

    
#Useful links:
#https://www.programiz.com/python-programming/datetime/strptime
#https://www.studytonight.com/python-howtos/how-to-convert-a-datetime-object-to-seconds