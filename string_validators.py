def string_validators(string):
    #Es un numero
    print(any (c.isalnum() for c in string))
    #Esta alfebeticamente ordenada
    print(any (c.isalpha() for c in string))
    #Es un numero
    print(any(c.isdigit() for c in string))
    #Esta en minusculas
    print(any(c.islower() for c in string))
    #Esta en mayusculas
    print(any(c.isupper() for c in string))

    
    


if __name__ == '__main__':
    string = input()
    string_validators(string)
