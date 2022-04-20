def mod_Divmod(n1:int,n2:int):
    dividor_modulo = divmod(n1,n2)
    for i in dividor_modulo:
        print(i)
    print(dividor_modulo)


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    mod_Divmod(n1,n2)