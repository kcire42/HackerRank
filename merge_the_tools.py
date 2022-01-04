def main(texto,divisible):
    zipped = zip(*[iter(texto)]*3)
    print(zipped)

    

if __name__ == "__main__":
    # cadena = input()
    # divisor = int(input())
    # main(cadena,divisor)
    lis1 = [1, 2, 3, 4, 5]
 
    # printing type
    print("The list is of type : " + str(type(lis1)))
    
    # converting list using iter()
    lis1 = iter(lis1)
    
    # printing type
    print("The iterator is of type : " + str(type(lis1)))
    
    # using next() to print iterator values
    print(next(lis1))
    print(next(lis1))
    print(next(lis1))
    print(next(lis1))
    print(next(lis1))
    print(lis1)