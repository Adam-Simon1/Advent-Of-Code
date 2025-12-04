lines = open("./Day 4/Part 1/input.txt").read().splitlines()

finalcnt = 0
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

print(finalcnt)
