def main():
    # n = int(input())
    # # numeros = hash(tuple((map(int, input().split()))))
    # # print(numeros)
    # print(input() == 0 or hash(tuple([int(x) for x in (input().strip().split())])))
    # # input()
    # # print(hash(tuple(int(x) for x in input().split())))
    n = int(input())
    integer_list = hash(tuple(map(int, input().split())))
    print(integer_list)
    
    


if __name__ == '__main__':
    main()