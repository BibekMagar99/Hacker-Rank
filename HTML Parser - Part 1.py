# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:56:59 2021

@author: bibek
"""

#This code works on python2 only as there is no module called HTMPparser in python3
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print 'Start :', tag
        for element in attrs:
            print '->', element[0], '>', element[1]

    def handle_endtag(self, tag):
        print 'End   :', tag

    def handle_startendtag(self, tag, attrs):
        print 'Empty :', tag
        for element in attrs:
            print '->', element[0], '>', element[1]
N = int(raw_input())
a =""
for i in range(N):
    a += raw_input()
parser = MyHTMLParser()
parser.feed(a)
