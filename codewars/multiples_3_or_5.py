def solution(number):
    result = 0
    for n in range(number):
        if n % 3 == 0:
            result += n
        elif n % 5 == 0:
            result += n

    return result
