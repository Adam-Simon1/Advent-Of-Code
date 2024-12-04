lines = open('Day 1/Part 1/input.txt').read().splitlines()

lines = [line.split() for line in lines]

right = []
left = []
for line in lines:
    right.append(int(line[0]))
    left.append(int(line[1]))

counter = {}
for num in left:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

s = 0
for num in right:
    s += num * counter[num] if num in counter else 0

print(s)
