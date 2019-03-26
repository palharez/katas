# Description:
# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(alist):
    pair = {alist.index(n): n for n in alist if n % 2 == 0}
    odds = sorted([n for n in alist if n % 2 != 0])
    for k, v in pair.items():
        odds.insert(k, v)
    return odds

print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))