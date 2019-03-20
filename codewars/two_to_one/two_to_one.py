def longest(s1, s2):
    return "".join(sorted(set(s1+s2)))

if __name__ == "__main__":
    print(longest("aretheyhere", "yestheyarehere"))
    print(longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu")
    print(longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy")