import  numpy as np
def main():
    n, m = list(map(int,input().split()))
    a = np.array([input().split() for _ in range(n)],dtype=int)
    #print(n)
    #print(m)
    #print(a)
    sum = np.sum(a,axis = 0)
    prod = np.prod(sum,axis=None) 
    print(prod)


if __name__ == '__main__':
    main()