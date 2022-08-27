import  numpy as np

def main():
    n,m = list(map(int,input().split()))
    a = np.array([input().split() for i in range(n)],dtype=int)
    print(np.mean(a,axis=1))
    print(np.var(a,axis=0))
    print(round(np.std(a,axis=None),11))

if __name__ == '__main__':
    main()