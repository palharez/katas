"""
Kyu Rank: 6

Winter is coming, you must prepare your ski holidays. 
The objective of this kata is to determine the number of pair of gloves 
you can constitute from the gloves you have in your drawer.

A pair of gloves is constituted of two gloves of the same color.

You are given an array containing the color of each glove.

You must return the number of pair you can constitute.

You must not change the input array.

Examples :

my_gloves = ["red","green","red","blue","blue"]
number_of_pairs(my_gloves) == 2; # red and blue

red_gloves = ["red","red","red","red","red","red"];
number_of_pairs(red_gloves) == 3; # 3 red pairs
"""

def number_of_pairs(gloves):
    validated = []

    pairs = 0

    for glove in gloves:
        counted = gloves.count(glove)

        if glove not in validated:
            pairs += counted // 2
            validated.append(glove)

    return pairs

if __name__ == '__main__':
    assert  number_of_pairs(["red","red"]) == 1
    assert  number_of_pairs(["red","green","blue"]) == 0
    assert  number_of_pairs(["gray","black","purple","purple","gray","black"]) == 3
    assert  number_of_pairs([]) ==0
    assert  number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]) == 4