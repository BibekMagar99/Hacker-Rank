#import the library 
from itertools import combinations_with_replacement

#taking the two inputs, string and the iterator
inp,n = input().split()

#string and the iterator
A = list(combinations_with_replacement(inp,int(n)))
joined_list = []
#joining the tuples
for i in A:
    joined_list.append("".join(sorted(i)))
#sorting the joined elements
B = sorted(joined_list)
for i in B:
    print(i)
    