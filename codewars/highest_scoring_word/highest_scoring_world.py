def high(string):
    words = string.split()
    highest_word = ''
    highest_value = 0
    for word in words:
        value = word_value(word)
        if value > highest_value:
            highest_value = value
            highest_word = word

    return highest_word


def word_value(word):
    return sum([ord(w) - 96 for w in word])


if __name__ == "__main__":
    print(high('man i need a taxi up to ubud'))  # 'taxi'
    print(high('what time are we climbing up the volcano'))  # 'volcano'
    print(high('take me to semynak'))  # 'semynak'
