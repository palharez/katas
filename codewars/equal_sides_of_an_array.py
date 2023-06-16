def find_even_index(arr):
    if len(arr) == 0:
        return 0
    
    summed = sum(arr)
    summing = 0
    
    for i in range(len(arr)):
        summed -= arr[i]
        
        if summed == summing:
            return i
        
        summing += arr[i]
        
    return -1
