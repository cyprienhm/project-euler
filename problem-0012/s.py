from itertools import count
from math import inf, sqrt
from multiprocessing import Pool

w = 1000


def number_divisors(n):
    c = 2
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            c += 2
    return c


def check_range(args):
    l, h = args
    for n in range(l, h):
        t = n * (n + 1) // 2
        if number_divisors(t) >= 500:
            return t
    return None


def solve():
    with Pool(processes=14) as p:
        for res in p.imap(check_range, ((low, low + w) for low in count(1, w))):
            if res is not None:
                return res


def main():
    print(solve())


if __name__ == "__main__":
    main()
