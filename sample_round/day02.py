with open("sample_round/day02.txt") as f:
    d = [eval(booly.title()) for booly in f.read().splitlines()]

def even_and_odd_or(d):
    return [d[i] and d[i+1] if i%4==0 else d[i] or d[i+1] \
            for i in range(0, len(d), 2)]

def part1():
    return sum([i+1 if j else 0 for i, j in enumerate(d)])

def part2():
    return even_and_odd_or(d).count(True)

def part3(d):
    tot = d.count(True)
    while len(d) > 1:
        d = even_and_odd_or(d)
        tot += d.count(True)

    return tot



print("Part 1:", part1())
print("Part 2:", part2())
print("Part 3:", part3(d))