if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
#taking Input
    a=tuple(integer_list)
#type conversion to tuple
    print(hash(a))
#printing Hash
