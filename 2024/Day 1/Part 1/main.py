lines = open('Day 1/Part 1/input.txt').read().splitlines()

lines = [line.split() for line in lines]

right = []
left = []
for line in lines:
    right.append(int(line[0]))
    left.append(int(line[1]))

right = sorted(right)
left = sorted(left)

s = 0
for i in range(len(right)):
    s += abs(right[i] - left[i])

print(s)
