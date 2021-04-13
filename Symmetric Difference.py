M = int(input())
elements_1 = set(input().split())
N = int(input())
elements_2 = set(input().split())
#all taking inputs

final_1 = elements_1.difference(elements_2)
#doing a-b

final_2 = elements_2.difference(elements_1)
#doing b-a


ok = final_1.union(final_2)
#doing a union b


last = sorted(list(map(int,ok)))
#converting all elements to integer -> making it a list  -> sorting
for i in last:
    print(i)
    
#printing line by line

