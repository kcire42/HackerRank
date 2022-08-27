import numpy as np

def main():
    n,m,p = list(map(int,input().split()))
    n_p = np.array([input().split() for _ in range(n)],dtype=int)
    m_p = np.array([input().split() for _ in range(m)],dtype=int)
    print(np.concatenate((n_p,m_p),axis=0))


if __name__ == '__main__':
    main()