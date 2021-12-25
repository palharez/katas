def square_digits(num):
    """
    Kyu Rank: 7

    Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

    For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

    Note: The function accepts an integer and returns an integer
    """
    parsed_number = str(num)
    
    print(num)
    
    total = []
    
    for number in parsed_number:
        np = int(number)
        sqr_num = np*np
        total.append(str(sqr_num))
    
    return int(''.join(total))

if __name__ == "__main__":
    assert square_digits(9119) == 811181
    assert square_digits(0) == 0
