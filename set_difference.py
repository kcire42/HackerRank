<<<<<<< HEAD
#No regresa la diferencia de las listas
def set_difference(numero_1:int,set_1:set,numero_2:int,set_2:set)->int:
    diferencia = set_1.difference(set_2)
    return len(diferencia)

if __name__ == "__main__":
    numero_1 = int(input())
    set_1 = set(map(int,input().split()))
    numero_2 = int(input())
    set_2 = set(map(int,input().split()))
    diferencia = set_difference(numero_1,set_1,numero_2,set_2)
    print(diferencia)
=======
#No regresa la diferencia de las listas
def set_difference(numero_1:int,set_1:set,numero_2:int,set_2:set)->int:
    diferencia = set_1.difference(set_2)
    return len(diferencia)

if __name__ == "__main__":
    numero_1 = int(input())
    set_1 = set(map(int,input().split()))
    numero_2 = int(input())
    set_2 = set(map(int,input().split()))
    diferencia = set_difference(numero_1,set_1,numero_2,set_2)
    print(diferencia)
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
    