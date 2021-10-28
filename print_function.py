def main(n):
    lista = ""
    for i in range(1,n+1):
        lista += str(i)
    print(lista)


if __name__ == '__main__':
    n = int(input())
    main(n)