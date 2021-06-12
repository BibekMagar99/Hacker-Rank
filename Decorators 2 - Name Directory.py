# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 22:57:06 2021

@author: bibek
"""

import operator
def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people, key = lambda x: (int(x[2])))]
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')