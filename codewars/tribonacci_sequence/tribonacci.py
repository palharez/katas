def tribonacci(signature, n):
    vector_tribonacci = signature[:]
    for i in range(n):
        aux = sum(signature)
        signature.pop(0)
        signature.append(aux)
        vector_tribonacci.append(aux)
        if len(vector_tribonacci) == n:
            break
    return [vector_tribonacci[k] for k in range(n)]


if __name__ == "__main__":
    print(tribonacci([1, 1, 1], 10))
