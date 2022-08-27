<<<<<<< HEAD
def main():
    cantidad_a = int(input())
    conjunto_a = set(map(int,input().split()))
    cantidad_b = int(input())
    conjunto_b = set(map(int,input().split()))
    # print(conjunto_a)
    # print(conjunto_b)
    conjunto_a_b = conjunto_a.symmetric_difference(conjunto_b)
    #print(conjunto_a_b)
    conjunto_a_b_sorted = sorted(conjunto_a_b)
    for i in conjunto_a_b_sorted:
        print(i)
    
    
    



if __name__ == "__main__":
    main()


=======
def main():
    cantidad_a = int(input())
    conjunto_a = set(map(int,input().split()))
    cantidad_b = int(input())
    conjunto_b = set(map(int,input().split()))
    # print(conjunto_a)
    # print(conjunto_b)
    conjunto_a_b = conjunto_a.symmetric_difference(conjunto_b)
    #print(conjunto_a_b)
    conjunto_a_b_sorted = sorted(conjunto_a_b)
    for i in conjunto_a_b_sorted:
        print(i)
    
    
    



if __name__ == "__main__":
    main()


>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
# 71839139  