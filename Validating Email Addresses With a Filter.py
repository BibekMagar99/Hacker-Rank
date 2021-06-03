# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:37:51 2021

@author: bibek
"""
import re
def fun(s):
    if re.match(r"[a-zA-Z0-9-_]+\@[a-zA-Z0-9]+\.[a-z]{1,3}$",s):
        return s
    else:
        pass
        
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)