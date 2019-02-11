def sum_two_smallest_numbers(numbers):
    lows = []
    low = numbers[0]
    i = 0
    while True:
        if low >= numbers[i]:
            low = numbers[i]
        if numbers[i] == numbers[-1]:
            lows.append(low)
            numbers.remove(low)
            low = numbers[0]
            i = 0       
        if len(lows) >= 2:
            return lows[0] + lows[1]
        i += 1
