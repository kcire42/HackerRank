import  numpy as np

def main():
    n,m = list(map(int,input().split()))
    n_m = np.array([input().split() for _ in range(n)],dtype = int)
    print(np.transpose(n_m))
    print(n_m.flatten())

if __name__ == '__main__':
    main()