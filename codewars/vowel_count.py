def get_count(sentence):
    """
    Kyu Rank: 7

    Return the number (count) of vowels in the given string.

    We will consider a, e, i, o, u as vowels for this Kata (but not y).

    The input string will only consist of lower case letters and/or spaces.
    """
    vowels = 'aeiou'
    qty = 0
    
    for world in sentence:
        if world in vowels:
            qty += 1
    
    return qty


if __name__ == "__main__":
    assert get_count('y') == 1
    assert get_count('abracadabra') == 5