#from itertools import product
import itertools

def producto_cruz(vector_A,vector_B):
    producto_cruz = itertools.product(vector_A,vector_B)
    #print(*product(vector_A,vector_B))
    print(*producto_cruz)
    


if __name__ == "__main__":
    vector_A = list(map(int,input().split()))
    vector_B = list(map(int,input().split()))
    producto_cruz(vector_A,vector_B)