from functools import cache

n = 3**37


@cache
def f(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 3:
        return 3
    if x % 2 == 0:
        return f(x // 2)
    if (x - 1) % 4 == 0:
        x = x // 4
        return 2 * f(2 * x + 1) - f(x)
    if (x - 3) % 4 == 0:
        x = x // 4
        return 3 * f(2 * x + 1) - 2 * f(x)


def s(n):
    q, r = divmod(n, 4)
    return (
        6
        + sum(6 * f(2 * k + 1) - 3 * f(k) + f(k + 1) for k in range(1, q))
        + sum(f(k) for k in range(4 * q + 1, n + 1))
    )


@cache
def s_recur(n):
    """Recurrent relation of S.

    This was found by writing writing that:
    n = 4q + r
    S(n) = sum 1 to 4q f(k) + sum 4q+1 to n f(k)
                              ^^^^^^^^^^^^^^^^^^ constant stuff
    the first sum can be rewritten as
    sum 0 to q-1 f(4k+1) + f(4k+2) + f(4k+3) + f(4k+4)
    every term can be replaced with the recurrence relation
    then by reordering and identifying S, you get that
    S(n) = constant stuff + 6S(2q-1) - 7f(1) - 9f(q) - 8S(q)
    """
    if n < 16:
        return s(n)
    q, r = divmod(n, 4)
    return (
        6
        + sum(f(k) for k in range(4 * q + 1, n + 1))
        + 6 * s_recur(2 * q - 1)
        - 7 * f(1)
        + 9 * f(q)
        - 8 * s_recur(q)
    )


print(str(s_recur(n))[-9:])
