if __name__ == '__main__':
    N = int(input())
#how many times to run the loop
    arr = []
#creating an empty list
    for i in range (0,N):
#loop
        cmd, *tup = input().split()
#take the beginning as command and later as a list
        if cmd == 'print' :
#separate print caused problem and was not compatible so this was added
            a = cmd + '(arr)'
#string concatenation 
            eval(a)
#execution of a string
        else :
            ftup = str(tuple(map(int,tup)))
# the later inputs i.e integers converted into integers then tuple then string
            final = 'arr.' + cmd + ftup
#string concatenation
            eval(final)
