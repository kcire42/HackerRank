def split_and_join(line):
    lista = line.split(" ")
    union = "-".join(lista)
    return union



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)