from itertools import product


def palindrome(n):
    s = str(n)
    l = len(s)
    for i in range(l // 2 + 1):
        if s[i] != s[l - 1 - i]:
            return False
    return True


found = 0
for a, b in product(range(100, 1000), range(100, 1000)):
    if palindrome(a * b):
        found = max(found, a * b)

print(found)
