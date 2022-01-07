""""
Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tess.
"""

def first_non_repeating_letter(string):
    for letter in string:
        if letter.isalpha():
            lower_letter = letter.lower()
            upper_letter = letter.upper()

            count_lower = string.count(lower_letter)
            count_upper = string.count(upper_letter)

            if count_lower == 1 and count_upper == 0:
                return letter

            if count_upper == 1 and count_lower == 0:
                return letter
        else:
            if string.count(letter) == 1:
                return letter

    return ''

if __name__ == '__main__':
    print('should handle simple tests')
    print(first_non_repeating_letter('a'), 'a')
    print(first_non_repeating_letter('stress'), 't')
    print(first_non_repeating_letter('moonmen'), 'e')

    print('should handle empty strings')
    print(first_non_repeating_letter(''), '')

    print('should handle all repeating strings') 
    print(first_non_repeating_letter('abba'), '')
    print(first_non_repeating_letter('aa'), '')

    print('should handle odd characters')
    print(first_non_repeating_letter('~><#~><'), '#')
    print(first_non_repeating_letter('hello world, eh?'), 'w')

    print('should handle letter cases')
    print(first_non_repeating_letter('sTreSS'), 'T')
    print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')