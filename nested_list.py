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
            
    #print(lista)
    #dejar solo el segundo lugar
    # segundo_lugar = [lista[1]]
    #print(segundo_lugar[0][1])
    #algoritmo para revisar si hay empates en alguna posicion
    # for participante in range(len(lista[2::])):
    #     #print(lista[participante+2][1])
    #     if segundo_lugar[0][1] == lista[participante+2][1]:
    #        segundo_lugar.append(lista[participante+2])  
    #print(segundo_lugar)
    segundo_lugar = []
    for participante in range(len(lista)):
        #print(lista[0][1])
        if lista[0][1] < lista[participante][1]:
            segundo_lugar.append(lista[participante])
    segundo_lugar_correcto = [segundo_lugar[0]]
    for participante_2 in range(len(segundo_lugar[1::])):
        #print(lista[participante+2][1])
        if segundo_lugar_correcto[0][1] == segundo_lugar[participante_2+1][1]:
           segundo_lugar_correcto.append(segundo_lugar[participante_2+1])  
    #print(segundo_lugar_correcto)

    #print(segundo_lugar)
    segundo_lugar_correcto.sort()
    for nombres in range(len(segundo_lugar_correcto)):
        print(segundo_lugar_correcto[nombres][0])


if __name__ == '__main__':
    main()
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# kakunami
# 19
# Vikas
# 21

    
    