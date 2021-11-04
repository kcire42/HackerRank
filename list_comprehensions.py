def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    #listas = []
    listas = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)  if a + b + c != n ]
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range (z+1):
    #             for w in range(n+1):
    #                 listas.append([i,j,k,n])


    print(listas)


    
        







if __name__ == '__main__':
    main()
    