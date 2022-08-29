def check_strict_superset():
    super_group_A = set(map(int,input().split()))
    numbers_of_group = int(input())
    count = 0 
    for group in range(numbers_of_group):
        group = set(map(int,input().split()))
        status_group = group.issubset(super_group_A)
        if status_group == True:
            count += 1

    if count == numbers_of_group:
        print("True")
    else:
        print("False")
    


if __name__ == '__main__':
    check_strict_superset()