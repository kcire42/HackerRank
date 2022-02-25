
# d = defaultdict(list)
# list1=[]

# n, m = map(int,raw_input().split())

# for i in range(0,n):
#     d[raw_input()].append(i+1) 

# for i in range(0,m):
#     list1=list1+[raw_input()]  

# for i in list1: 
#     if i in d:
#         print " ".join( map(str,d[i]) )
#     else:
#         print -1


def main():
    d = defaultdict(list)
    n, m = map(int, input().split())
    lista = []
    for i in range(0,n):
        d[input()].append(i+1)
    #print(d)
    for j in range(0,m):
        lista = lista + [input()]
    #print(lista)
    for k in lista:
        if k in d:
            print (" ".join(map(str,d[k])))
        else:
            print(-1)
        
        

    


if __name__ == "__main__":
    main()
