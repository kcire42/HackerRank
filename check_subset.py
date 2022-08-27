def check_subset():
    numbers_of_groups = int(input())
    answers = []
    for grupo in range(numbers_of_groups):
        numero_elementos_A = int(input())
        elementos_A = set(map(int,input().split()))
        numero_elementos_B = int(input())
        elementos_B = set(map(int,input().split()))
        answers.append(elementos_A.issubset(elementos_B))
    for answer in answers:
        print(answer)




if __name__ == "__main__":
    check_subset()