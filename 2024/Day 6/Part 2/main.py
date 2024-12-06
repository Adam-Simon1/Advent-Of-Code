lines = open('Day 6/Part 1/input.txt').read().splitlines()

location = (0, 0)
location_start = (0, 0)
for l, line in enumerate(lines):
    lines[l] = list(line)
    for c, char in enumerate(line):
        if char == '^':
            location = (l, c)
            location_start = (l, c, 0)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()
d = 0

while True:
    row, col = location

    new_row, new_col = row + directions[d][0], col + directions[d][1]

    if len(lines) == new_row or len(lines[0]) == new_col:
        break
    elif lines[new_row][new_col] == '#':
        d += 1

        if d == 4:
            d = 0
    else:
        location = (new_row, new_col)
        visited.add(location)


def check(location, lines):
    d = 0
    visited_2 = set()

    while True:
        row, col, _ = location

        new_row, new_col = row + directions[d][0], col + directions[d][1]

        if new_row < 0 or new_row >= len(lines) or new_col < 0 or new_col >= len(lines[0]):
            return 0

        if (new_row, new_col, d) in visited_2:
            return 1

        if lines[new_row][new_col] == '#':
            d = (d + 1) % 4
        else:
            location = (new_row, new_col, d)
            visited_2.add(location)


total = 0
for location in visited:
    lines_temp = [row.copy() for row in lines]
    lines_temp[location[0]][location[1]] = '#'
    total += check(location_start, lines_temp)

print(total)
