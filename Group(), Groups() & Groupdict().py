# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:38:18 2021

@author: bibek
"""
import re
S = input()
pattern = r'([a-zA-Z0-9])\1+'
m = re.search(pattern,S)
print(m.group(1) if m else -1)