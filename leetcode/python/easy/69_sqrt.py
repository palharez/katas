def my_sqrt(target: int) -> int:
    if target == 0:
        return 0

    left = 1
    right = target
    ans = 0

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == target:
            return mid
        elif square < target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


if __name__ == "__main__":
    assert my_sqrt(8) == 2
    assert my_sqrt(4) == 2
    assert my_sqrt(2) == 1

