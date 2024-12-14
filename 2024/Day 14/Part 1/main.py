lines = open('Day 14/Part 1/input.txt').read().splitlines()

grid_size = (103, 101)
count = {}

for line in lines:
    pos, vel = line.split()

    pos = pos.split('p=')[1]
    vel = vel.split('v=')[1]

    y, x = pos.split(',')
    vy, vx = vel.split(',')

    x, y, vx, vy = int(x), int(y), int(vx), int(vy)

    for s in range(100):
        x = (x + vx) % grid_size[0]
        y = (y + vy) % grid_size[1]

    if (x, y) not in count:
        count[(x, y)] = 1
    else:
        count[(x, y)] += 1

forbid_row = (grid_size[0]) // 2
forbid_col = (grid_size[1]) // 2

quadrants = {
    ((0, 0), (forbid_row-1, forbid_col-1)): 0,
    ((0, forbid_col+1), (forbid_row-1, grid_size[1])): 0,
    ((forbid_row+1, 0), (grid_size[0], forbid_col-1)): 0,
    ((forbid_row+1, forbid_col+1), (grid_size[0], grid_size[1])): 0
}

safety_factor = 1
for (x, y), amount in count.items():
    if x == forbid_row or y == forbid_col:
        continue

    for quad in quadrants:
        start_x, start_y = quad[0]
        end_x, end_y = quad[1]

        if start_x <= x <= end_x and start_y <= y <= end_y:
            quadrants[quad] += amount

for quad in quadrants.values():
    safety_factor *= quad

print(safety_factor)
