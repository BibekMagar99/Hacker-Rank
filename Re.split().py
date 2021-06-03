# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:27:40 2021

@author: bibek
"""

regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

'''
[,.]     :   Square brackets specifies a set of characters you wish to match.
+        :   The plus symbol + matches one or more occurrences of the pattern left to it.