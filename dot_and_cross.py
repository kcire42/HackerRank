import numpy 

def main():
    # A = []
    # B = []
    # for i in range (int(input())):
    #     matriz_0 = list(map(int,input().split()))
    #     matriz_1 = list(map(int,input().split()))
    #     A.append(matriz_0)
    #     A.append(matriz_1)
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)],dtype =int)
    b = numpy.array([input().split() for _ in range(n)],dtype= int)
    m = numpy.dot(a,b)
    print(m)


if __name__ == '__main__':
    main()