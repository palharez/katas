"""
Time: O(s+t)
Memory: O(s+t)

Contamos a quantidade de cada letra em cada uma das strings e no final comparamos se possuem a mesma
quantidade sendo assim um anagram.

To match the anagram, we count and save every element in the strings, at the end we compare if the
characters quantities are equal.
"""

def isAnagram(s: str, t: str) -> bool:
    t_letter_counter = {}
    s_letter_counter = {}

    for c in s:
        if s_letter_counter.get(c):
            s_letter_counter[c] += 1
        else:
            s_letter_counter[c] = 1

    for c in t:
        if t_letter_counter.get(c):
            t_letter_counter[c] += 1
        else:
            t_letter_counter[c] = 1

    return t_letter_counter == s_letter_counter


if __name__ == '__main__':
    assert isAnagram('anagram', 'nagaram') == True
    assert isAnagram('rat', 'car') == False

