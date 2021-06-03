# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:31:08 2021

@author: bibek
"""

import re
N = int(input())
for i in range(N):
    a = input()
    pattern = '^[-+]?[0-9]*\.[0-9]+$'
    
    '''
    ^     :  The caret symbol ^ is used to check if a string starts with a certain character.
    [-+]  :  Square brackets specifies a set of characters you wish to match.
     ?    :  The question mark symbol ? matches zero or one occurrence of the pattern left to it.
    [0-9] :  Matches any decimal digit
    *     :  The star symbol * matches zero or more occurrences of the pattern left to it.
    \.    :  Matches if the . is at the start of a string. 
    +     :  The plus symbol + matches one or more occurrences of the pattern left to it.
    $     :  The dollar symbol $ is used to check if a string ends with a certain character.
    '''
    print(bool(re.match(pattern, a)))