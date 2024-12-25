lines = open('Day 25/Part 1/input.txt').read().split('\n\n')

lines = [line.splitlines() for line in lines]
locks = set()
keys = set()

for grid in lines:
    config = []
    is_lock = grid[0].count('#') == len(grid[0])

    for col in list(zip(*grid)):
        height = col.count('#')

        config.append((len(col) - height - 1) if is_lock else height-1)

    if is_lock:
        locks.add(tuple(config))
    else:
        keys.add(tuple(config))

total = 0
for lock in locks:
    for key in keys:
        if all(k <= l for k, l in zip(key, lock)):
            total += 1

print(total)
