import numpy

def main():
    pass
    # a = numpy.array([input().split() for _ in range(n)],dtype =int)
    # b = numpy.array([input().split() for _ in range(n)],dtype= int)
    a = numpy.array([input().split() for _ in range(1)],dtype=int)
    b = numpy.array([input().split() for _ in range(1)],dtype=int)
    print(int(numpy.inner(a,b)))
    print(numpy.outer(a,b))

if __name__ == '__main__':
    main()