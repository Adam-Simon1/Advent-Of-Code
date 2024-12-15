lines = open('Day 15/Part 1/input.txt').read().splitlines()
grid = []

for l, line in enumerate(lines):
    if line == '':
        break

    grid.append(list(line))

instructions = lines[l+1:]
instructions = "".join(instructions)

pos = ()
for l, line in enumerate(grid):
    for c, char in enumerate(line):
        if grid[l][c] == '@':
            pos = (l, c)
            grid[l][c] = '.'

directions = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
slice_map = {
    '>': lambda: grid[pos[0]][pos[1]+1:],
    '<': lambda: grid[pos[0]][:pos[1]][::-1],
    'v': lambda: list(zip(*grid))[pos[1]][pos[0]+1:],
    '^': lambda: list(zip(*grid))[pos[1]][:pos[0]][::-1],
}

for inst in instructions:
    new_pos = (pos[0] + directions[inst][0], pos[1] + directions[inst][1])
    new_char = grid[new_pos[0]][new_pos[1]]

    if new_char == '#':
        continue

    if new_char == 'O':
        space = slice_map[inst]()
        empty_space = space.count('.')

        if empty_space == 0:
            continue

        for i in range(len(space)):
            if space[i] == '#':
                break

            if space[i] == '.':
                grid[new_pos[0] + directions[inst][0] *
                     i][new_pos[1] + directions[inst][1] * i] = 'O'

                grid[new_pos[0]][new_pos[1]] = '.'
                pos = new_pos

                break

    if new_char == '.':
        pos = new_pos

total = 0
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == 'O':
            total += 100 * r + c

print(total)
