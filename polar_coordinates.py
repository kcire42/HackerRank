import cmath
def main():
    imagionario = complex(input())
    print(abs(complex(imagionario)))
    print(cmath.phase(complex(imagionario)))
    


if __name__ == "__main__":
    main()
