import numpy 
def main():
    n,m = list(map(int,input().split()))
    a = numpy.array([input().split() for _ in range(n)],dtype=int)
    b = numpy.array([input().split() for _ in range(n)],dtype=int)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(numpy.mod(a,b))
    print(a**b)



if __name__ == '__main__':
    main()