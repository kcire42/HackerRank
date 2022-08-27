
def set_discard_remove_pop():
    data = int(input())
    lista = set(map(int,input().split()))
    instructions = int(input())
    #print(lista)
    for trys in range(instructions):
        instruction = list(map(str,input().split()))
        #print(instruction[0])
        if instruction[0] == "remove":
            lista.remove(int(instruction[1]))
        elif instruction[0] == "discard":
            lista.discard(int(instruction[1]))
        elif instruction[0] == "pop":
            lista.pop()
        #print(lista)
    count = 0 
    for i in lista:
        count +=int(i)
    print(count)
    


        


if __name__ == "__main__":
    set_discard_remove_pop()