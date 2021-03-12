def split_and_join(line):
    return("-".join(line.split(" ")))
#it first splits at spaces and then join the strings using -

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
