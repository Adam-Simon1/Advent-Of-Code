lines = open("./Day 4/Part 1/input.txt").read().splitlines()

new_grid = [list(line) for line in lines]
lines = [list(line) for line in lines]

answer = 0
while True:
    finalcnt = 0
    new_grid = [row[:] for row in lines]

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                          (1, 0), (1, -1), (0, -1), (-1, -1)]

            if lines[r][c] != '@':
                continue

            cnt = 0
            for dr, dc in directions:
                x, y = r + dr, c + dc

                if not (0 <= x < len(lines) and 0 <= y < len(lines[r])):
                    continue

                if lines[x][y] == '@':
                    cnt += 1

            if cnt < 4:
                finalcnt += 1
                new_grid[r][c] = '.'

    answer += finalcnt

    if finalcnt == 0:
        break

    lines = new_grid


print(answer)
