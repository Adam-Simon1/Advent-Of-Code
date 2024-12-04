from collections import Counter

lines = open('Day 4/Part 1/input.txt').read().splitlines()

total = 0
for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[0]) - 1):
        if lines[row][col] != 'A':
            continue

        corners = [lines[row-1][col-1], lines[row-1][col+1],
                   lines[row+1][col+1], lines[row+1][col-1]]

        cnt = Counter(corners)

        if corners[0] == corners[2] or corners[1] == corners[3]:
            continue

        if cnt['M'] == 2 and cnt['S'] == 2:
            total += 1

print(total)
