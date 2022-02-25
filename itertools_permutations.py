from itertools import permutations
def main(palabra, numero):
    permutaciones = list(permutations(palabra,numero))
    permutaciones = sorted(permutaciones)
    
    for permutacion in permutaciones:
        print("".join(permutacion))


if __name__ == "__main__":
    palabra, numero = input().split()
    numero = int(numero)
    main(palabra,numero)