
def solve(s):
    lista = s.split()
    for i in lista:
        s = s.replace(i,i.capitalize())
    return s
    
    
        
    

if __name__ == '__main__':
    s = input()
    result = solve(s)

    