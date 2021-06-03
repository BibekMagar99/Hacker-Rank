# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:22:52 2021

@author: bibek
"""
#Had to look it up
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))