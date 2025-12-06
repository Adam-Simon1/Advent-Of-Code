import math

lines = open("./Day 6/Part 1/input.txt").read().splitlines()

for l, line in enumerate(lines):
    line = line.split(' ')

number_cols = list(zip(*lines))

number_cols = [list(filter(lambda x: x.strip(), col)) for col in number_cols]

cols = []
last = 0
for c, col in enumerate(number_cols):
    if col == []:
        cols.append(number_cols[last:c])
        last = c + 1
cols.append(number_cols[last:])

result = 0
for col in cols:
    operation = None
    nums = []

    for num in col:
        if ('*' in num) or ('+' in num):
            operation = num[-1]
            num = num[:-1]

        nums.append(int("".join(num)))

    if operation == '*':
        result += math.prod(nums)
    else:
        result += sum(nums)


print(result)
