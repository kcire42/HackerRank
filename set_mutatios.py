
def set_mutatios():
    number_of_datas = int(input())
    data = set(map(int,input().split()))
    number_of_instructions = int(input())
    for i in range(number_of_instructions):
        instruction = list(map(str,input().split()))
        new_set = set(map(int,input().split()))
        if instruction[0] == "intersection_update":
            data.intersection_update(new_set)   
        elif instruction[0] == "update":
            data.update(new_set)
        elif instruction[0] == "symmetric_difference_update":
            data.symmetric_difference_update(new_set)
        elif instruction[0] == "difference_update":
            data.difference_update(new_set)
    count = 0 
    for j in data:
        count +=int(j)
    print(count)
    


if __name__ == "__main__":
    set_mutatios()