# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:42:13 2021

@author: bibek
"""
def solve(s):
#It splits the sentence at (space) and creates a list.
    ok = s.split(" ")

#capitalize() makes the first letter of the passed argument capital, 
#if sentence is passed then the first letter of the sentence is only capitalized
#if word is passed then only the first letter of the word is capitalized
    lk = [i.capitalize() for i in ok]


#it joins the elements of the list with " " (space)
    return (" ".join(lk))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()