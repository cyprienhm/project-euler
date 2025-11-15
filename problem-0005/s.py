from functools import reduce


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    rm2, rm1 = a, b

    while rm1 != 0:
        rm2, rm1 = rm1, divmod(rm2, rm1)[1]
    return rm2


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


print(reduce(lambda t, c: lcm(t, c), [i for i in range(1, 21)], 1))
