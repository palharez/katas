import re


def order(sentence):
    sentence_arr = sentence.split()
    return ' '.join(sorted(sentence_arr, key=lambda word: re.findall(r'\d', word)))


if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
    print(order("4of Fo1r pe6ople g3ood th5e the2"),
          "Fo1r the2 g3ood 4of th5e pe6ople")
    print(order(""), "")
