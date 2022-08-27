<<<<<<< HEAD
from itertools import permutations
def main(palabra, numero):
    permutaciones = list(permutations(palabra,numero))
    permutaciones = sorted(permutaciones)
    
    for permutacion in permutaciones:
        print("".join(permutacion))


if __name__ == "__main__":
    palabra, numero = input().split()
    numero = int(numero)
=======
from itertools import permutations
def main(palabra, numero):
    permutaciones = list(permutations(palabra,numero))
    permutaciones = sorted(permutaciones)
    
    for permutacion in permutaciones:
        print("".join(permutacion))


if __name__ == "__main__":
    palabra, numero = input().split()
    numero = int(numero)
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
    main(palabra,numero)