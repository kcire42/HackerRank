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
    print(result)