"""
Solving valid palindrome challenge with two pointers technique
"""

def is_palindrome(s):
  if len(s) == 1:
    return True

  parsed_s = s.lower()
  filtered_s = list(filter(lambda n: n.isalnum(), parsed_s))

  i = 0
  j = len(filtered_s) - 1

  while i < j:
    if filtered_s[i] != filtered_s[j]:
      return False

    i += 1
    j -= 1

  return True

if __name__ == '__main__':
  print(is_palindrome("A man, a plan, a canal: Panama"), True)
  print(is_palindrome("race a car"), False)
  print(is_palindrome(""), True)
