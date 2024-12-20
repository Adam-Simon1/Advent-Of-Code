grid = open('Day 20/Part 1/input.txt').read().splitlines()

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == 'S':
            start = (r, c)
            break
    else:
        continue
    break

q = [(start)]
visited = {start}
dists = {start: 0}

while q:
    x, y = q.pop(0)

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
            continue

        if grid[nx][ny] == '#':
            continue

        if (nx, ny) in visited:
            continue

        q.append((nx, ny))
        visited.add((nx, ny))
        dists[(nx, ny)] = dists[(x, y)] + 1

        if grid[nx][ny] == 'E':
            break

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == '#':
            continue
        for r in range(2, 21):
            for dx in range(r + 1):
                dy = r - dx

                for nx, ny in {(x + dx, y + dy), (x + dx, y - dy), (x - dx, y + dy), (x - dx, y - dy)}:
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                        continue

                    if grid[nx][ny] == '#':
                        continue

                    imp = dists[(x, y)] - dists[(nx, ny)]

                    if imp >= 100 + r:
                        count += 1

print(count)
