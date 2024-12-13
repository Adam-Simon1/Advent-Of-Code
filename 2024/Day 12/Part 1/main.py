lines = open('./Day 12/Part 1/input.txt').read().splitlines()

visited = set()
regions = []

for r, row in enumerate(lines):
    for c, crop in enumerate(row):
        if (r, c) in visited:
            continue

        visited.add((r, c))

        queue = [(r, c)]
        region = set()
        region.add((r, c))

        while queue:
            x, y = queue.pop(0)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < len(lines) and 0 <= ny < len(lines[0])):
                    continue

                new = lines[nx][ny]

                if new != crop:
                    continue

                if (nx, ny) in region:
                    continue

                region.add((nx, ny))
                queue.append((nx, ny))
                visited.add((nx, ny))

        regions.append(region)


price = 0
for region in regions:
    total = len(region) * 4

    for x, y in region:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(lines) and 0 <= ny < len(lines[0])):
                continue

            if (nx, ny) in region:
                total -= 1

    price += total * len(region)

print(price)
