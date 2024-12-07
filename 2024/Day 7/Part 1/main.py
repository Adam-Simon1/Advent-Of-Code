import operator

lines = open('Day 7/Part 1/input.txt').read().splitlines()

lines = [line.split() for line in lines]
ops = {"+": operator.add, "*": operator.mul}


def evaluate(vals, line, line_i):
    current = int(line[line_i])
    new_vals = []

    for i in range(len(vals)):
        for op in ['+', '*']:
            new_vals.append(ops[op](vals[i], current))

    if len(line) == line_i + 1:
        return new_vals
    else:
        return evaluate(new_vals, line, line_i + 1)


total = 0
for line in lines:
    vals = []
    for op in ['+', '*']:
        vals.append(ops[op](int(line[1]), int(line[2])))

    if len(line) > 3:
        result = evaluate(vals, line, 3)
    else:
        result = vals

    e_total = int(line[0].replace(':', ''))
    if e_total in result:
        total += e_total

print(total)
