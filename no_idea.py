def no_idea(len_n:int , len_m:int, m:set, a:set, b:set):
    count = 0 
    for element in m: 
        if element in a:
            count += 1
        elif element in b:
            count -= 1
        else:
            count += 0 
    print(count)




if __name__ == '__main__':
    len_n, len_m = list(map(int,input().split()))
    m = list(map(int,input().split()))
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    no_idea(len_n,len_m,m,a,b)
