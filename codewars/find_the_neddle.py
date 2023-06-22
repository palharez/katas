def find_needle(haystack):
    for i, hay in enumerate(haystack):
        if hay == 'needle':
            return f'found the needle at position {i}'
