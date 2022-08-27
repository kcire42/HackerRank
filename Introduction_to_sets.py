<<<<<<< HEAD
def average(array):
    # your code goes here
    #print(array)
    total = 0 
    for i in array:
     #   print(i)
        total += i 
    #print(total)
    average = total/len(array)
    
    return average
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
=======
def average(array):
    # your code goes here
    #print(array)
    total = 0 
    for i in array:
     #   print(i)
        total += i 
    #print(total)
    average = total/len(array)
    
    return average
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
    print(result)