from functools import cache

lines = open('./Day 19/Part 1/input.txt').read().splitlines()

colors = lines[:1][0].split(',')
towels = lines[2:]
colors = sorted(colors, key=len)[::-1]
colors = [color.strip() for color in colors]


@cache
def check(towel):
    if not towel:
        return True

    for color in colors:
        if towel.startswith(color):
            remaining = towel[len(color):]

            if check(remaining):
                return True

    return False


total = 0
for towel in towels:
    total += check(towel)

print(total)
