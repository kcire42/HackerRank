def main():
    n = int(input())
    numeros = list(map(int,input().split()))
    #print(numeros)
    lista = ordanamiento(numeros)
    #print(lista)
    segundo = str(lista[1])
    print(segundo)
    

    
    

def ordanamiento(our_list):

    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list)-1):
            if our_list[j] < our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
    return our_list

if __name__ == '__main__':
    main()
    
