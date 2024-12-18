import heapq

lines = open('Day 18/Part 1/input.txt').read().splitlines()

lines = [line.split(',') for line in lines]
lines = [[int(x) for x in line] for line in lines]

width = 71

grid = [['.' for _ in range(width)] for _ in range(width)]


def check(grid, lines, index):
    for i in range(index):
        y, x = lines[i]
        grid[x][y] = '#'

    start = (0, 0)
    end = (width-1, width-1)

    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))
    visited = {}
    visited[start] = 0

    while pq:
        cost, x, y = heapq.heappop(pq)

        if (x, y) == end:
            return

        if cost > visited[(x, y)]:
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < width and 0 <= ny < width):
                continue

            if grid[nx][ny] == '#':
                continue

            if grid[nx][ny] == '.':
                new_cost = cost + 1
                if (nx, ny) not in visited or new_cost < visited[(nx, ny)]:
                    heapq.heappush(pq, (new_cost, nx, ny))
                    visited[(nx, ny)] = new_cost

    return -1


for i in range(1024, len(lines)):
    if check(grid, lines, i) == -1:

        print(lines[i-1])
        break
