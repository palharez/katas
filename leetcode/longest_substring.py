def lengthOfLongestSubstring(s):
  s_list = []
  max_length = 0

  for n in s:
    if n in s_list:
      s_list = s_list[s_list.index(n)+1:]

    s_list.append(n)
    max_length = max(max_length, len(s_list))
  
  return max_length


if __name__ == '__main__':
  print(lengthOfLongestSubstring('abcabcbb')) # abc 3
  print(lengthOfLongestSubstring('bbbbb')) # b 1
  print(lengthOfLongestSubstring('pwwkew')) # wke 3
  print(lengthOfLongestSubstring(' ')) # 1
  print(lengthOfLongestSubstring('ohvhjdml')) # 6
  print(lengthOfLongestSubstring('')) # 0
  print(lengthOfLongestSubstring('aab')) # 2
  print(lengthOfLongestSubstring('dvdf')) # 2


