def longest_palindrome(s):
    asw = ''
    for i in range(len(s)):
        for n in range(i, len(s)):
            string = s[i:n+1]
            if is_palindrome(string) and len(string) > len(asw):
                asw = string

    return asw


def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


if __name__ == "__main__":
    print(longest_palindrome('babad'))  # 'bab' 'aba'
    print(longest_palindrome('cbbd'))  # 'bb'
    print(longest_palindrome('xabay'))  # 'bb'
