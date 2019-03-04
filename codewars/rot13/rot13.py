from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    cipherRot13 = ''
    for letter in message:
        if letter == letter.lower():
            cipherRot13 += _lower(letter)
        else:
            cipherRot13 += _upper(letter)
    return cipherRot13

def _upper(letter):
    pos = ascii_uppercase.index(letter)
    index = n = pos
    while True:
        if index == len(ascii_uppercase):
            index = 0
        if n == pos + 13:
            break
        index += 1
        n += 1
    return ascii_uppercase[index]


def _lower(letter):
    pos = ascii_lowercase.index(letter)
    index = n = pos
    while True:
        if index == len(ascii_lowercase):
            index = 0
        if n == pos + 13:
            break
        index += 1
        n += 1
    return ascii_lowercase[index]

if __name__ == "__main__":
    print(rot13('Test') == 'Grfg')
