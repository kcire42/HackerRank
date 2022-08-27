<<<<<<< HEAD
#une los tipos de datos de los dos set
def set_union(cantidad_1 : int , lista_1 : set , cantidad_2 : int , lista_2 : set ) -> int :
    conjunto = lista_1.union(lista_2)
    return len(conjunto)
    

    


if __name__ == "__main__":
    cantidad_1 = int(input())
    lista_1 = set(map(int,input().split()))
    cantidad_2 = int(input())
    lista_2 = set(map(int,input().split()))
    print(set_union(cantidad_1 ,lista_1, cantidad_2 , lista_2 ))
=======
#une los tipos de datos de los dos set
def set_union(cantidad_1 : int , lista_1 : set , cantidad_2 : int , lista_2 : set ) -> int :
    conjunto = lista_1.union(lista_2)
    return len(conjunto)
    

    


if __name__ == "__main__":
    cantidad_1 = int(input())
    lista_1 = set(map(int,input().split()))
    cantidad_2 = int(input())
    lista_2 = set(map(int,input().split()))
    print(set_union(cantidad_1 ,lista_1, cantidad_2 , lista_2 ))
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
