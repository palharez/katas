def move_zeros(array):
    """
    Kyu Rank: 5

    Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    """
    zeros_arr = []
    new_arr = []
    
    for number in array:
        if number == 0:
            zeros_arr.append(number)
        else:
            new_arr.append(number)
            
    new_arr.extend(zeros_arr)
    
    return new_arr


if __name__ == "__main__":
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) ==  [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros( [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros([0, 0,]) == [0, 0]
    assert move_zeros([]) == []