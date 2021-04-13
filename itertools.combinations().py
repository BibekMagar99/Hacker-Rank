from itertools import combinations
#importing the library

#taking the input "string" and "repeatition"
item, n = input().split()
n = int(n)


for i in range (1,n+1):
    #creating empty list for each iteration
    A =[]
    b = list(combinations(item,i))
    
    #converting the element to list -> sorting the elements in the list -> joining them to make a full string
    #finally appemding them to the empty list A
    for i in b:
        A.append("".join(sorted(list(i))))
        
    #sorting the final appended list
    A = sorted(A)
    
    #printing them one by one
    for i in A:
        print(i)
        
