from itertools import *
def main(palabra,numero):
    combinaciones = list(combinations_with_replacement(palabra,numero))
    nueva_combinacion = []
    for combinacion in combinaciones:
        combinacion = sorted(combinacion)
        nueva_combinacion.append(combinacion)
        #print("".join(combinacion))
    nueva_combinacion = sorted(nueva_combinacion)
    for elemento in nueva_combinacion:
        print("".join(elemento))


    


if __name__ == "__main__":
    palabra, numero = input().split()
    numero = int(numero)
    main(palabra, numero)