def shuffle(s, indices):
    response = [0] * len(indices)

    for i in range(len(s)):
        word = s[i]
        indice = indices[i]
        response[indice] = word

    return ''.join(response)



if __name__ == '__main__':
    print(shuffle(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
    print(shuffle(s="", indices=[]))
