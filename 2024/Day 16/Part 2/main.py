import heapq
from collections import defaultdict

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
    parents = defaultdict(list)

    heapq.heappush(queue, (0, start[0], start[1], 0))
    costs[(start[0], start[1], 0)] = 0
    parents[(start[0], start[1], 0)] = [None]

    min_cost = float('inf')

    while queue:
        cost, x, y, d = heapq.heappop(queue)

        if cost > min_cost:
            break

        if (x, y) == end:
            min_cost = cost
            continue

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
                    parents[(nx, ny, i)] = [(x, y, d)]
                elif new_cost == costs[(nx, ny, i)]:
                    parents[(nx, ny, i)].append((x, y, d))

    distinct_locations = set()

    def backtrack(state):
        x, y, d = state
        distinct_locations.add((x, y))
        if state == (start[0], start[1], 0):
            return

        for parent in parents[state]:
            if parent is not None:
                backtrack(parent)

    for d in range(4):
        if (end[0], end[1], d) in parents:
            backtrack((end[0], end[1], d))

    return len(distinct_locations)


print(djikstra(grid, start, end))
