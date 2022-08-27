<<<<<<< HEAD
#from itertools import product
import itertools

def producto_cruz(vector_A,vector_B):
    producto_cruz = itertools.product(vector_A,vector_B)
    #print(*product(vector_A,vector_B))
    print(*producto_cruz)
    


if __name__ == "__main__":
    vector_A = list(map(int,input().split()))
    vector_B = list(map(int,input().split()))
=======
#from itertools import product
import itertools

def producto_cruz(vector_A,vector_B):
    producto_cruz = itertools.product(vector_A,vector_B)
    #print(*product(vector_A,vector_B))
    print(*producto_cruz)
    


if __name__ == "__main__":
    vector_A = list(map(int,input().split()))
    vector_B = list(map(int,input().split()))
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
    producto_cruz(vector_A,vector_B)