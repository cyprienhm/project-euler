def collatz_len(n):
    chain = 1
    while n != 1:
        chain += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return chain


highest = 1
highest_i = 1
for i in range(1, 1_000_000):
    l = collatz_len(i)
    if l > highest:
        highest = l
        highest_i = i

print(highest_i)
