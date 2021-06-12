# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:36:01 2021

@author: bibek
"""
#This too python2 as python3 doesnot have HTMLParser module

from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for elements in attrs: 
            print"-> "+elements[0]+" > "+str(elements[1])
    def handle_endtag(self, tag):
        #print("End   : "+tag)
        pass
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for elements in attrs: 
            print"-> "+elements[0]+" > "+str(elements[1])

parser = MyHTMLParser()
N = int(raw_input())
for _ in range(N):
    a = raw_input()
    parser.feed(a)