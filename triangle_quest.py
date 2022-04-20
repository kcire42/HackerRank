def triangle_quest(amount):
    for i in range(1,amount):
        s = (str(i)*i)
        print(int(s))


if __name__ == "__main__":
    amount = int(input())
    triangle_quest(amount)