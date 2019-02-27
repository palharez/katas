def find_it(seq):
    for n in seq:
        odd = 0
        for j in seq:
            if n == j:
                odd += 1
        if odd % 2 != 0:
            return n

if __name__ == "__main__":
    print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5)
