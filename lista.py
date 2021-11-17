def main():
    numero_instrucciones = int(input())
    lista = []
    for instruccion in range(numero_instrucciones):
        instruccion_a_ejecutar = list(input().split())
        print(instruccion_a_ejecutar)


if __name__=='__main__':
    main()