def three_consecutive_odds(arr: List[int]) -> bool:
    consecutives = []

    for n in arr:
        if len(consecutives) == 3:
            return true

        if n % 2 != 0:
            consecutives.append(n)
        else:
            consecutives = []

    return len(consecutives) == 3
