# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 12:08:29 2021

@author: bibek
"""

import re
N = int(input())

for i in range(N):
    num = input()
    #checking if it starts with 4,5 or 6 and has remaining 15 digits or each four digits are separated by -
    if bool(re.match(r"^[456]\d{15}", num)) or bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num)):

        num = num.replace("-", "")
        #checking if there are four consecutive repetition
        if bool(re.match(r"(?!.*(\d)(-?\1){3})", num)):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")