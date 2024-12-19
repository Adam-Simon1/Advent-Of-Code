from functools import cache

lines = open('./Day 19/Part 1/input.txt').read().splitlines()

colors = lines[:1][0].split(',')
towels = lines[2:]
colors = sorted(colors, key=len)[::-1]
colors = [color.strip() for color in colors]


@cache
def check(towel):
    if not towel:
        return 1

    arragements = 0
    for color in colors:
        if towel.startswith(color):
            remaining = towel[len(color):]
            arragements += check(remaining)

    return arragements


total = 0
for towel in towels:
    total += check(towel)

print(total)
