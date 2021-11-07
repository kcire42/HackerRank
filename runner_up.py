def main():
    n = int(input())
    numeros = map(int,input().split())
    #print(numeros)
    lista = ordanamiento(list(numeros))
    #print(lista)
    segundo = lista[1]

    print(segundo)
    

    
    

def ordanamiento(our_list):
    
   
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] < our_list[j+1]:
                # Swap
                
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
    print(our_list)
    lista_sin_repetidos = []
    for numero in our_list:
        if not numero in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)
    print(lista_sin_repetidos)
    
        




if __name__ == '__main__':
    main()
    
