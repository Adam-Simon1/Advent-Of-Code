# Another approach, using compression, since lower entropy = lower size of compressed string

import zlib
import sys

lines = open('Day 14/Part 1/input.txt').read().splitlines()

grid_size = (103, 101)

points = []
for line in lines:
    pos, vel = line.split()
    pos = pos.split('p=')[1]
    vel = vel.split('v=')[1]
    y, x = pos.split(',')
    vy, vx = vel.split(',')
    points.append((int(x), int(y), int(vx), int(vy)))

smallest = (10e9, 0)

grid = [['.' for _ in range(grid_size[1])] for _ in range(grid_size[0])]

for second in range(8000):
    for x, y, vx, vy in points:
        new_x = (x + vx * second) % grid_size[0]
        new_y = (y + vy * second) % grid_size[1]
        grid[new_x][new_y] = '#'

    string = ''
    for row in grid:
        string += ''.join(row)

    compressed = zlib.compress(string.encode('utf-8'))
    size = len(compressed)

    if size <= smallest[0]:
        smallest = (size, second)

    grid = [['.' for _ in range(grid_size[1])] for _ in range(grid_size[0])]

print(smallest)
