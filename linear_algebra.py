import numpy 
def main():
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)],dtype=float)
    #det = numpy.linalg.det(a)
    print(round(numpy.linalg.det(a),2))
    


if __name__ == '__main__':
    main()