lines = open('Day 10/Part 1/input.txt').read().splitlines()

starts = []
for l, line in enumerate(lines):
    for h, height in enumerate(line):
        if height == '0':
            starts.append((l, h))

total_score = 0
for start in starts:
    trails = set()
    queue = [(start[0], start[1], [f"{start[0]}{start[1]}"])]

    while queue:
        cx, cy, path = queue.pop(0)
        current = int(lines[cx][cy])

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if not (0 <= nx < len(lines) and 0 <= ny < len(lines[0])):
                continue

            coord = f"{nx}{ny}"
            if coord in path:
                continue

            next_height = int(lines[nx][ny])

            if next_height == current + 1:
                new_path = path + [coord]

                if next_height == 9:
                    trails.add(tuple(new_path))
                else:
                    queue.append((nx, ny, new_path))

    total_score += len(trails)

print(total_score)
