from math import sqrt


def factors(n):
    found = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            found.append(i)

    return found


number = 600851475143


print(max(filter(lambda x: len(factors(x)) == 0, factors(number))))
