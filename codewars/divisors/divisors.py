def divisors(integer):
    k = [n for n in range(2, integer) if integer % n == 0]
    return k if k != [] else "%i is prime" % integer


if __name__ == "__main__":
    print(divisors(13))
