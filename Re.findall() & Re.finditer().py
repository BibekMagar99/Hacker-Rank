# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:35:55 2021

@author: bibek
"""

import re
S = input()
#  ?<= is lookbehind
m = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])',S)
if m:
    for i in m:
        print(i)
else:
    print(-1)