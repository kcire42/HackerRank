import numpy  
def main():
    a = numpy.array(input().split(),dtype=float)
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))


if __name__ == '__main__':
    main()