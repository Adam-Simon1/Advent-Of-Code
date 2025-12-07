grid = open("./Day 7/Part 1/input.txt").read().splitlines()

start = (0, 0)
for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        start = (0, i)
        break

q = [start]
beams = set()
cnt = 0
while q:
    r, c = q.pop()

    if r == len(grid) - 1:
        continue

    if (r, c) in beams:
        continue

    beams.add((r, c))

    if grid[r][c] == '^':
        cnt += 1
        q.insert(0, (r, c - 1))
        q.insert(0, (r, c + 1))
    else:
        q.insert(0, (r + 1, c))

print(cnt)
