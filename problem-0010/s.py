max_n = 2_000_000
sieves = {i: True for i in range(2, max_n)}

for elt in sieves.keys():
    n = 2 * elt
    while n < max_n:
        sieves[n] = False
        n += elt

primes = [i for i, v in sieves.items() if v]
print(sum(primes))
