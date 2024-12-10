lines = open('Day 10/Part 1/input.txt').read().splitlines()

starts = []
for l, line in enumerate(lines):
    for h, height in enumerate(line):
        if height == '0':
            starts.append((l, h))

total_score = 0
for start in starts:
    visited = set()
    queue = [start]
    score = 0

    while queue:
        cx, cy = queue.pop(0)

        current = int(lines[cx][cy])

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if not (0 <= nx < len(lines) and 0 <= ny < len(lines[0])):
                continue

            if (nx, ny) in visited:
                continue

            next_height = int(lines[nx][ny])

            if next_height == current + 1:
                if next_height == 9:
                    score += 1
                    visited.add((nx, ny))
                    continue

                queue.append((nx, ny))
                visited.add((nx, ny))

    total_score += score

print(total_score)
