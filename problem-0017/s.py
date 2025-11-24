twenty2w = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


tens2w = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def num2word(n):
    if n == 0:
        return ""
    if n in twenty2w:
        return twenty2w[n]

    digits = [int(c) for c in str(n)]
    ans = ""
    if n < 100:
        follow = n % 10
        if follow == 0:
            return tens2w[digits[0]]
        return tens2w[digits[0]] + " " + num2word(n % 10)
    elif n < 1000:
        follow = n % 100
        if follow == 0:
            return twenty2w[digits[0]] + " hundred"
        return twenty2w[digits[0]] + " hundred and " + num2word(n % 100)
    elif n < 10000:
        follow = n % 1000
        before = n // 1000
        if follow == 0:
            return num2word(before) + " thousand"
        return num2word(before) + " thousand " + num2word(follow)


print(sum(len(num2word(i).replace(" ", "")) for i in range(1, 1001)))
