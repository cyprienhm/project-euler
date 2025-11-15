def first_n_sum(n):
    return n * (n + 1) / 2


def first_n_2_sum(n):
    return 1 / 3 * (n * n * n + 3 / 2 * n * n + n / 2)


print(first_n_sum(100) ** 2 - first_n_2_sum(100))
