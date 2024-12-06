lines = open('Day 6/Part 1/input.txt').read().splitlines()

location = (0, 0)
for l, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '^':
            location = (l, c)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()
visited.add(location)
d = 0

while True:
    row, col = location

    new_row, new_col = row + directions[d][0], col + directions[d][1]

    if len(lines) == new_row or len(lines[0]) == new_col:
        break
    elif lines[new_row][new_col] == '#':
        d = (d + 1) % 4
    else:
        location = (new_row, new_col)
        visited.add(location)

print(len(visited))
