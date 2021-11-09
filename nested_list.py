def main():
    lista =[]
    for ingreso_de_datos in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
    #print(lista)
    #algoritmo para ordenar los datos de menor a mayor 
    for i in range(len(lista)):
        # print(lista[i])
        # print(lista[i][1])
        for j in range(len(lista)-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j] , lista[j+1] = lista[j+1], lista[j]
            
    print(lista)
    #dejar solo el segundo lugar
    segundo_lugar = [lista[1]]
    #print(segundo_lugar[0][1])
    #algoritmo para revisar si hay empates en alguna posicion
    for participante in range(len(lista[2::])):
        #print(lista[participante+2][1])
        if segundo_lugar[0][1] == lista[participante+2][1]:
           segundo_lugar.append(lista[participante+2])
       

        
    print(segundo_lugar)


if __name__ == '__main__':
    main()
    
    