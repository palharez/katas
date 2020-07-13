
SYMBOL_VAlUE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

VALUE_SYMBOL = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


class RomanNumerals:

    def to_roman(n):
        roman = ''
        for a in reversed(sorted(VALUE_SYMBOL.keys())):
            while (a <= n):
                n = n - a
                roman = roman + VALUE_SYMBOL[a]
        return roman

    def from_roman(roman_number):
        sum = 0

        for number_pos in range(len(roman_number)):

            value = SYMBOL_VAlUE[roman_number[number_pos]]
            next_value = SYMBOL_VAlUE[roman_number[number_pos + 1]
                                      ] if number_pos < len(roman_number) - 1 else 0

            if value < next_value:
                sum -= value
            else:
                sum += value

        return sum
