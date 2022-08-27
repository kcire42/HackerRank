<<<<<<< HEAD
#envia los numeros que no estan en ambas listas 
def set_symmetric_difference(numero_1:int,set_1:set,numero_2:int,set_2:set)->int:
    simetria = set_1.symmetric_difference(set_2)
    return len(simetria)


if __name__ == "__main__":
    numero_1 = int(input())
    set_1 = set(map(int,input().split()))
    numero_2 = int(input())
    set_2 = set(map(int,input().split()))
    simetria = set_symmetric_difference(numero_1,set_1,numero_2,set_2)
    print(simetria)
=======
#envia los numeros que no estan en ambas listas 
def set_symmetric_difference(numero_1:int,set_1:set,numero_2:int,set_2:set)->int:
    simetria = set_1.symmetric_difference(set_2)
    return len(simetria)


if __name__ == "__main__":
    numero_1 = int(input())
    set_1 = set(map(int,input().split()))
    numero_2 = int(input())
    set_2 = set(map(int,input().split()))
    simetria = set_symmetric_difference(numero_1,set_1,numero_2,set_2)
    print(simetria)
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
