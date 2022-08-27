<<<<<<< HEAD
from itertools import combinations 
def main(palabra,numero):
    print("hola")
    combinaciones = list(combinations(palabra,numero))
    combinaciones = sorted(combinaciones)
    for combinacion in combinaciones:
        print(combinacion)


if __name__ == "__main__":
    palabra , numero = input().split()
    numero = int(numero)
=======
from itertools import combinations 
def main(palabra,numero):
    print("hola")
    combinaciones = list(combinations(palabra,numero))
    combinaciones = sorted(combinaciones)
    for combinacion in combinaciones:
        print(combinacion)


if __name__ == "__main__":
    palabra , numero = input().split()
    numero = int(numero)
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
    main(palabra,numero) 