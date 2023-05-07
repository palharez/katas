def count(allowed: str, words: [str]) -> int:
    """
    O(Words)
    """
    allowed = {s: True for s in allowed}

    counter = 0

    for word in words:
        validated = True

        for char in word:
            if not allowed.get(char):
                validated = False
                break

        if validated:
            counter += 1

    return counter


if __name__ == '__main__':
    print(count(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]), 2)
    print(count(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]), 4)
    print(count(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]), 7)
