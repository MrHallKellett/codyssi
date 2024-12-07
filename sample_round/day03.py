from string import ascii_lowercase as LOW
from string import ascii_uppercase as UP
DIG = "".join(str(i) for i in range(10))
BASE_65_DIGITS = (DIG + UP + LOW + "!@#")

with open("sample_round/day03.txt") as f:
    d = [(row.split()[0], int(row.split()[1])) \
         for row in f.read().splitlines()]

def part1():
    return sum(r[1] for r in d)

def part2():
    return sum(int(r[0], r[1]) for r in d)


def b652b10(val):
    return BASE_65_DIGITS.index(val)

def b102b65(val):
    return BASE_65_DIGITS[val]

def oops():
    e=enumerate
    r=reversed
    return sum(sum([b102b65(val) * (i**65) \
                    for i, val in e(r(row[0]))]) for row in d)

def part3():
    tot = part2()
    col = 0
    while 65 ** col < tot:
        col += 1
    col -= 1
    result = ""
    while col >= 0:
        digit, tot = divmod(tot, 65**col)
        col -= 1
        result += b102b65(digit)
        print(result)


print("Part 1:", part1())
print("Part 2:", part2())
print("Part 3:", part3())
