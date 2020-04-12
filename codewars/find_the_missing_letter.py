def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i]) + 1 < ord(chars[i+1]):
            return chr(ord(chars[i]) + 1)

    return chr(ord(chars[-1]) + 1)


if __name__ == "__main__":
    print(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
    print(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
