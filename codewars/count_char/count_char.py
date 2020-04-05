def count(string):
    asw = {}

    for char in string:
        occurrences = string.count(char)
        asw[char] = occurrences
        
        string.replace(char, '')

    return asw
