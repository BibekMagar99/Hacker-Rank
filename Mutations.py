def mutate_string(string, position, character):
    s = list(string)
    s[position] = str(character)
    return ''.join(s)
    
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
