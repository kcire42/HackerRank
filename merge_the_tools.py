def main(texto,divisible):
    #zipped = zip(*[iter(texto)]*divisible)
    for _ in zip(*[iter(texto)]*divisible):        
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in _ if c not in d]))
    

    

if __name__ == "__main__":
    # cadena = input()
    # divisor = int(input())
    # main(cadena,divisor)
    # # lis1 = "AAABCADDE"
 
    # # # printing type
    # # print("The list is of type : " + str(type(lis1)))
    
    # # # converting list using iter()
    # # lis1 = zip(*[iter(lis1)]*3)
    
    # # # printing type
    # # print("The iterator is of type : " + str(type(lis1)))
    
    # # # using next() to print iterator values
    # # print(next(lis1))
    # # print(next(lis1))
    # # print(next(lis1))
    texto = input()
    divisible = int(input())
    main(texto,divisible)
    