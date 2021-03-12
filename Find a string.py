def count_substring(string, sub_string):
    ok =0
    totallen = len(string)
    sublen = len(sub_string)
    for i in range(0, totallen):
#loops until the end according to the substring
        if sub_string == string[i:(i+sublen)]:
#print(string[i:(i+sublen)]) to see what is happening
#compares the string by breaking continuously with size equal to the substring+1
#i.e CBCBC so the comparision must be with CBC -> BCB ->CBC
            ok = ok +1
    return ok
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
