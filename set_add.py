def main():
    cantidad = int(input())
    registro = set()
    for i in range(cantidad):
        pais = input()
        registro.add(pais)
    print(len(registro))


if __name__ == "__main__":
    main()