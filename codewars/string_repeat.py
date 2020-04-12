def repeat_str(repeat, string):
    return repeat * string


if __name__ == "__main__":
    print(repeat_str(4, 'a'), 'aaaa')
    print(repeat_str(3, 'hello '), 'hello hello hello ')
    print(repeat_str(2, 'abc'), 'abcabc')
