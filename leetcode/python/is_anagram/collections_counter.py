from collections import Counter

def is_anagram(s, t):
  if len(s) != len(t):
    return False

  s_counter = Counter(s)
  t_counter = Counter(t)

  for k, v in s_counter.items():
    if t_counter.get(k) != v:
      return False

  return True

if __name__ == '__main__':
  print(is_anagram('abc', 'cba'), True)
  print(is_anagram('a', 'ab'), False)
