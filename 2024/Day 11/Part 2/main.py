from functools import cache

line = open('./Day 11/Part 1/input.txt').read()

stones = line.split()


@cache
def calc(stone, steps):
    string = str(stone)
    length = len(string)

    if steps == 0:
        return 1
    elif stone == 0:
        return calc(1, steps - 1)
    elif len(string) % 2 == 0:
        return calc(int(string[:length // 2]), steps - 1) + calc(int(string[length // 2:]), steps - 1)
    else:
        return calc(stone * 2024, steps - 1)


print(sum(calc(int(stone), 75) for stone in stones))
