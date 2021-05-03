# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:00:17 2021

@author: bibek
"""
from collections import OrderedDict
def Splitter(string,n,factor):
    splitted_list = []
    for i in range(0,n,factor):
        splitted_list.append(string[i:i+factor])
    return splitted_list
        
    
    
def Duplicate_remover(child,factor):
    final_list = []
    for item in child:
        sanitized_list = []
        dictionary = OrderedDict()
        values = list(item)
        for i in values:
            if i in dictionary:
                dictionary[i]=dictionary[i]+1
            else:
                dictionary[i]=1
        for i in dictionary:
            sanitized_list.append(i)
        final_list.append("".join(sanitized_list))
    return final_list

                        
                    
        

string = input()
n = len(string)
factor = int(input())
child = Splitter(string,n,factor)
print(Duplicate_remover(child,factor))
