def no_idea(len_n:int , len_m:int, m:set, a:set, b:set):
    # add_happiness = m.intersection(a)
    # sub_happiness = m.intersection(b)
    # print(add_happiness)
    # print(sub_happiness)
    # count_happiness = len(add_happiness)-len(sub_happiness)
    # print(count_happiness)
    count_happines = 0
    for i in m:
        if i in a:
            count_happines += 1
        elif i in b:
            count_happines -= 1 
        else:
            count_happines += 0 
    return count_happines




if __name__ == '__main__':
    len_n, len_m = list(map(int,input().split()))
    m = set(map(int,input().split()))
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    print(no_idea(len_n,len_m,m,a,b))
    
