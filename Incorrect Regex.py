import re
n = int(input())
for i in range(n):
    a = input()
    # pattern is a string containing the regex pattern
    pattern = a
    
    try:
        re.compile(pattern)
        print("True")
    
    except re.error:
        print("False")