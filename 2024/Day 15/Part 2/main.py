lines = open('Day 15/Part 1/input.txt').read().splitlines()
grid = []

mapping = {
    '#': '##',
    '@': '@.',
    '.': '..',
    'O': '[]'
}

for l, line in enumerate(lines):
    if line == '':
        break

    new_line = ''
    for c, char in enumerate(line):
        new_line += mapping[char]

    grid.append(list(new_line))

instructions = lines[l+1:]
instructions = "".join(instructions)

pos = ()
for l, line in enumerate(grid):
    for c, char in enumerate(line):
        if grid[l][c] == '@':
            pos = (l, c)
            grid[l][c] = '.'

directions = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}


def check_around(pos, grid, direction):
    locations = [pos]
    queue = [pos]

    d = directions[direction]

    while queue:
        x, y = queue.pop(0)
        current = grid[x][y]

        nx = x + d[0]
        ny = y + d[1]

        if direction in ['>', '<']:
            if grid[x][ny] in ['[', ']'] and (x, ny) not in locations:
                locations.append((x, ny))
                queue.append((x, ny))
            elif grid[x][ny] == '#':
                return []
        elif direction in ['^', 'v']:
            if current == ']' and (x, y - 1) not in locations:
                locations.append((x, y - 1))
                queue.append((x, y - 1))
            elif current == '[' and (x, y + 1) not in locations:
                locations.append((x, y + 1))
                queue.append((x, y + 1))

            if grid[nx][y] in ['[', ']'] and (nx, y) not in locations:
                locations.append((nx, y))
                queue.append((nx, y))
            elif grid[nx][y] == '#':
                return []

    return locations


for inst in instructions:
    new_pos = (pos[0] + directions[inst][0], pos[1] + directions[inst][1])
    new_char = grid[new_pos[0]][new_pos[1]]

    if new_char == '#':
        continue

    if new_char == '[' or new_char == ']':
        dx, dy = directions[inst]
        locations = check_around(new_pos, grid, inst)
        grid_copy = [list(line) for line in grid]

        for x, y in locations:
            grid[x][y] = '.'

        for x, y in locations:
            grid[x + dx][y + dy] = grid_copy[x][y]

        if locations:
            pos = new_pos

    if new_char == '.':
        pos = new_pos

total = 0
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == '[':
            total += 100 * r + c

print(total)
