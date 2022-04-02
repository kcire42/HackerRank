def main():
    intentos : int = int(input())
    lista_numeros = []
    for intento in range(intentos):
        numeros = list(map(str,input().split()))
        lista_numeros.append(numeros)
    
    for numero in lista_numeros:
            try:
                numero_a, numero_b = int(numero[0]), int(numero[1])
                try:
                    division = numero_a/numero_b
                    print(int(division))
                except ZeroDivisionError:
                    print("Error Code: integer division or modulo by zero")
            except ValueError as e:
                print("Error Code:",e)

if __name__ == "__main__":
    main()