import numpy 
def main():
    #a = list(map(float,input().split()))
    a = numpy.array(input().split(),dtype=float)
    b = int(input())
    
    val = numpy.polyval(a,b)
    print(val)


if __name__ == '__main__':
    main()