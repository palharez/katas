def diagonalSum(mat):
    arr = {}

    result = 0

    k = len(mat) - 1

    for i in range(len(mat)):
        pos_i = '%s.%s' % (i, i)
        pos_k = '%s.%s' % (i, k)

        if not arr.get(pos_i):
            result += mat[i][i]
            arr[pos_i] = True

        if not arr.get(pos_k):
            result += mat[i][k]
            arr[pos_k] = True

        k -= 1

    return result

if __name__ == '__main__':
    print(diagonalSum(mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]))

    print(diagonalSum(mat=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
