import numpy as np

def main():
    n,m = list(map(int,input().split()))
    a = np.array([input().split() for _ in range(n)],dtype=int)
    k = int(input())
    k = k+1
    k1 =  m-k
    #print(k1)
    a_sort = a[np.argsort(a[:,k1])]
    for i in a_sort:
        print(*i,sep=' ')

if __name__ == '__main__':
    main()