def first_n(n: int):
    for i in range(n + 1):
        yield i * i


print(sum(filter(lambda x: x % 2 == 1, first_n(364_000))))
