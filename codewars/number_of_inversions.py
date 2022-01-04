def count_inversions(array):
    inversions = 0
    
    total = len(array)

    for i in range(total):
        comparator = array[i] 
        for j in range(i, total):
            compared = array[j]
            if comparator > compared:
                inversions += 1
    
    return inversions

if __name__ == '__main__':
    print(count_inversions([]), 0)
    print(count_inversions([1,2,3]), 0)
    print(count_inversions([2,1,3]), 1)
    print(count_inversions([6,5,4,3,2,1]), 15)
    print(count_inversions([6,5,4,3,3,3,3,2,1]), 30)