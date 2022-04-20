def integers_come_in_all_sizes(n1:int,n2:int,n3:int,n4:int)->int:
    return pow(n1,n2)+ pow(n3,n4)

if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    print(integers_come_in_all_sizes(n1,n2,n3,n4))