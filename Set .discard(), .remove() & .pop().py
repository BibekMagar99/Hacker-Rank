#integer input
n = int(input())

#creating a set
s = set(map(int, input().split()))

#integer N , the number of commands.
N = int(input())

for i in range(N):
    a = input()
    if a =="pop":
        try:
            s.pop()
        except:
            pass
    else:
        b = a.split(" ")
        if b[0]=="remove":
            try :
                s.remove(int(b[1]))
            except:
                pass
        elif b[0] == "discard":
            s.discard(int(b[1]))
            
print(sum(s))
            
        