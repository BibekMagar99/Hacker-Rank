if __name__ == '__main__':

    n = int(input())
    arr = map(int, input().split())

#map le duita argument lincha, euta function and arko chai iterable... so basically
#esle iterable bata chai tyo value lai function ma pass garcha..
#so hamro ma chai, input liyo ani space vako thau bata split garcha ani teslai
#int() ma pathaucha integer banauna.
    c = set(list(arr))
    c.remove(max(c))
    print(max(c))
