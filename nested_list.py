def main():
    lista =[]
    for ingreso_de_datos in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
    print(lista)
    for i in range(len(lista)):
        # print(lista[i])
        # print(lista[i][1])
        for j in range(len(lista)-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j][1] , lista[j+1][1] = lista[j+1][1] , lista[j][1]
                
    
    print(lista)


if __name__ == '__main__':
    main()
    
    