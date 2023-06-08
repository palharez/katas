def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    count = []
    
    for i in range(x, x * (n + 1), x):
        count.append(i)

    return count
