import math


def segmented_sieves(num_sieves):
    yielded = 0
    delta = int(math.sqrt(num_sieves)) + 2

    first_sieve = {i: True for i in range(2, 2 + delta)}

    for i, elt in first_sieve.items():
        mul = i * i
        while mul <= max(first_sieve.keys()):
            first_sieve[mul] = False
            mul += i

    sieves = [first_sieve]
    yield first_sieve

    while yielded < num_sieves:
        prev_higher = max(sieves[-1].keys()) + 1
        new_sieve = {i: True for i in range(prev_higher, prev_higher + delta)}

        for prev_sieve in sieves:
            for i, elt in prev_sieve.items():
                if elt:
                    mul = i * i
                    while mul <= prev_higher + delta:
                        if mul in new_sieve:
                            new_sieve[mul] = False
                        mul += i
        sieves.append(new_sieve)
        yield new_sieve
        yielded += 1


def first_n_primes(n):
    yielded = 0
    sieves = segmented_sieves(n * n)
    while yielded < n:
        next_sieve = next(sieves)
        for i, elt in next_sieve.items():
            if elt:
                yield i
                yielded += 1
                if yielded >= n:
                    return


print(max(first_n_primes(10_001)))
