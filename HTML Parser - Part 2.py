# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:24:17 2021

@author: bibek
"""
#This is also for python2
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if '\n' not in data:
                print(">>> Single-line Comment")
                print(data)
            else:
                print(">>> Multi-line Comment")
                print(data)
                
    def handle_data(self, data):
        if data != '\n': 
            print(">>> Data")
            print(data)

html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()