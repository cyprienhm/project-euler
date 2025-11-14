from itertools import takewhile


def fib():
    a = 1
    b = 2

    while True:
        yield a
        a, b = b, a + b


print(sum(filter(lambda x: x % 2 == 0, takewhile(lambda x: x <= 4_000_000, fib()))))
