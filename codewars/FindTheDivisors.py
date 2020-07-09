def divisors(integer):
    res = []

    for n in range(2, integer):
        if n > integer // 2:
            break

        if integer % n == 0:
            res.append(n)

    return res if res else "%s  is prime" % integer


if __name__ == "__main__":
    print(divisors(15))
    print(divisors(12))
    print(divisors(13))
