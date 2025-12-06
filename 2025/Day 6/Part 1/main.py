import math

lines = open("./Day 6/Part 1/input.txt").read().splitlines()

for l, line in enumerate(lines):
    line = line.split(' ')
    lines[l] = list(filter(None, line))

number_cols = list(zip(*lines))

result = 0
for col in number_cols:
    operation = col[-1]
    col = col[:-1]
    col = [int(x) for x in col]

    if operation == '*':
        result += math.prod(col)
    else:
        result += sum(col)

print(result)
