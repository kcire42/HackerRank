
import numpy as np

def main():
    n,m = list(map(int,input().split()))
    a = np.array([input().split() for i in range(n)],dtype=int)
    a_min = np.min(a,axis=1)
    print(np.max(a_min,axis=None))

if __name__ == "__main__":
    main()