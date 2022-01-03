"""
Kyu Rank: 6

Imagine that you went to a zoo and some zoologists asked you for help. 
They want you to find the strongest ape of its own kind and there are 4 types of apes in the zoo. (Gorilla, Gibbon, Orangutan, Chimpanzee)

There will be only one parameter which is a list containing lots of dictionaries.
Each dictionary will be like this: {"name": name, "weight": weight, "height": height, "type": type}
To find the strongest ape, you need to compare the sum of weight and height of each apes of that kind.
The ape with the highest weight and height will be the strongest ape.
You need to return a dictionary which contains the names of the strongest apes of all kinds.
    {"Gorilla": strongest_gorilla, "Gibbon": strongest_gibbon, "Orangutan": strongest_orangutan, "Chimpanzee": strongest_chimpanzee}
There can be 2 or more apes which has the same highest weight and height.
In that case, you need to sort their names by alphabet and then choose the first one as the strongest ape.
If there are no apes for a kind (e.g. Gorilla), you need to return a dictionary like this: 
    {"Gorilla": None, "Gibbon": strongest_gibbon, "Orangutan": strongest_orangutan, "Chimpanzee": strongest_chimpanzee}

Example 1:
find_the_strongest_apes(
            [{"name": "aba", "weight": 101, "height": 99, "type": "Gorilla"},
             {"name": "abb", "weight": 99, "height": 101, "type": "Gorilla"},
             {"name": "abc", "weight": 101, "height": 99, "type": "Orangutan"},
             {"name": "abd", "weight": 99, "height": 101, "type": "Orangutan"}])
Should return {'Gorilla': 'aba', 'Gibbon': None, 'Orangutan': 'abc', 'Chimpanzee': None}

Example 2:
find_the_strongest_apes(
            [{"name": "aba", "weight": 140, "height": 120, "type": "Gorilla"},
             {"name": "abb", "weight": 20, "height": 50, "type": "Gibbon"},
             {"name": "abc", "weight": 75, "height": 110, "type": "Orangutan"},
             {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}])
Should return {'Gorilla': 'aba', 'Gibbon': 'abb', 'Orangutan': 'abc', 'Chimpanzee': 'abd'}

Example 3:
find_the_strongest_apes(
            [{"name": "aba", "weight": 140, "height": 120, "type": "Gorilla"},
             {"name": "abb", "weight": 150, "height": 120, "type": "Gorilla"},
             {"name": "abc", "weight": 75, "height": 110, "type": "Orangutan"},
             {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}])
Should return {'Gorilla': 'abb', 'Gibbon': None, 'Orangutan': 'abc', 'Chimpanzee': 'abd'}
"""

def find_the_strongest_apes(apes):
    strongest = {
        "Gorilla": {'power': 0, 'name': None}, 
        "Gibbon": {'power': 0, 'name': None}, 
        "Orangutan": {'power': 0, 'name': None}, 
        "Chimpanzee": {'power': 0, 'name': None}
    }

    for ape in apes:
        ape_sum = ape.get('weight', 0) + ape.get('height', 0)
        if ape_sum > strongest[ape.get('type')].get('power'):
            strongest[ape.get('type')] = { 'name': ape['name'], 'power': ape_sum }

    return {k: v.get('name') for k, v in strongest.items()}

if __name__ == '__main__':
    print(find_the_strongest_apes(
    [{"name": "aba", "weight": 15, "height": 50, "type": "Gibbon"},
    {"name": "abb", "weight": 15, "height": 50, "type": "Gibbon"},
    {"name": "abc", "weight": 15, "height": 50, "type": "Gibbon"},
    {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}]), {'Gorilla': None, 'Gibbon': 'aba', 'Orangutan': None, 'Chimpanzee': 'abd'})
    print(find_the_strongest_apes(
    [{"name": "aba", "weight": 10, "height": 50, "type": "Gibbon"},
    {"name": "abb", "weight": 15, "height": 60, "type": "Gibbon"},
    {"name": "abc", "weight": 20, "height": 50, "type": "Gibbon"},
    {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}]), {'Gorilla': None, 'Gibbon': 'abb', 'Orangutan': None, 'Chimpanzee': 'abd'})
    print(find_the_strongest_apes(
    [{"name": "aba", "weight": 140, "height": 120, "type": "Gorilla"},
    {"name": "abb", "weight": 20, "height": 50, "type": "Gibbon"},
    {"name": "abc", "weight": 75, "height": 110, "type": "Orangutan"},
    {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}]), {'Gorilla': 'aba', 'Gibbon': 'abb', 'Orangutan': 'abc', 'Chimpanzee': 'abd'})
    print(find_the_strongest_apes(
    [{"name": "aba", "weight": 101, "height": 99, "type": "Gorilla"},
    {"name": "abb", "weight": 99, "height": 101, "type": "Gorilla"},
    {"name": "abc", "weight": 101, "height": 99, "type": "Orangutan"},
    {"name": "abd", "weight": 99, "height": 101, "type": "Orangutan"}]), {'Gorilla': 'aba', 'Gibbon': None, 'Orangutan': 'abc', 'Chimpanzee': None})
    print(find_the_strongest_apes(
    [{"name": "aba", "weight": 100, "height": 120, "type": "Gorilla"},
    {"name": "abb", "weight": 100, "height": 120.01, "type": "Gorilla"},
    {"name": "abc", "weight": 100, "height": 100, "type": "Orangutan"},
    {"name": "abd", "weight": 100.01, "height": 100, "type": "Orangutan"}]), {'Gorilla': 'abb', 'Gibbon': None, 'Orangutan': 'abd', 'Chimpanzee': None})