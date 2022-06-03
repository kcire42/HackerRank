import numpy
def main():
    num = list(map(int,input().split()))
    print(numpy.zeros(num,dtype=numpy.int))
    print(numpy.ones(num,dtype=numpy.int))

if __name__ == '__main__':
    main()