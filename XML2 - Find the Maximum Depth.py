# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:18:44 2021

@author: bibek
"""
#python2
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)
if __name__ == '__main__':
    n = int(raw_input())
    xml = ""
    for i in range(n):
        xml =  xml + raw_input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth