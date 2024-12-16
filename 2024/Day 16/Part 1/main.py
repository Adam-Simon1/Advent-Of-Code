import heapq

grid = open('Day 16/Part 1/input.txt').read().splitlines()

start = ()
end = ()

for l, line in enumerate(grid):
    for r, char in enumerate(line):
        if char == 'S':
            start = (l, r)

        if char == 'E':
            end = (l, r)


def djikstra(grid, start, end):
    queue = []
    costs = {}

    heapq.heappush(queue, (0, start[0], start[1], 0))
    costs[(start[0], start[1], 0)] = 0

    while queue:
        cost, x, y, d = heapq.heappop(queue)

        if (x, y) == end:
            return cost

        if cost > costs[(x, y, d)]:
            continue

        for i, (dx, dy) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                continue

            if grid[nx][ny] in ['.', 'E']:
                new_cost = cost + (1 if i == d else 1001)
                if (nx, ny, i) not in costs or new_cost < costs[(nx, ny, i)]:
                    costs[(nx, ny, i)] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny, i))

    return -1


print(djikstra(grid, start, end))
