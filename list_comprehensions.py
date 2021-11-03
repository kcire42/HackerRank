def main():
    x = int(input("Ingrese un numero x: "))
    y = int(input("Ingrese un numero y: "))
    z = int(input("Ingrese un numero z: "))
    n = int(input("Ingrese un numero n: "))

    if x > y and x > z:
        mayor = x+1
    elif y > x and y > z:
        mayor = y+1
    elif z > x and z > y: 
        mayor =z+1

    lista = []
    
    for i in range (mayor):
        lista.append([i])
        for j in range(mayor):
            lista[i].append(j)

    print(lista)


    
        







if __name__ == '__main__':
    main()
    