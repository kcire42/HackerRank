#regresa los numeros que estan en ambos puntos
def set_intersection(cantidad_1:int,set_1:set,cantidad_2:int,set_2:set)-> int:
    intersection = set_1.intersection(set_2)
    print(intersection)
    return len(intersection)


if __name__ == "__main__":
    cantidad_1 = int(input())
    set_1 = set(map(int,input().split()))
    cantidad_2 = int(input())
    set_2 = set(map(int,input().split()))
    print(set_intersection(cantidad_1,set_1,cantidad_2,set_2))