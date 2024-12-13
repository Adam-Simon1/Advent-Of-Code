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
    total = 0

    corners = set()
    for x, y in region:
        corners_loc = [(x - 0.5, y - 0.5), (x - 0.5, y + 0.5),
                       (x + 0.5, y + 0.5), (x + 0.5, y - 0.5)]
        for cx, cy in corners_loc:
            corners.add((cx, cy))

    for cx, cy in corners:
        new_squares = [(cx - 0.5, cy - 0.5), (cx - 0.5, cy + 0.5),
                       (cx + 0.5, cy + 0.5), (cx + 0.5, cy - 0.5)]
        positions = []

        for nx, ny in new_squares:
            positions.append((nx, ny) in region)

        if sum(positions) == 1:
            total += 1
        elif sum(positions) == 2:
            if (positions[0] + positions[2] == 2) or (positions[1] + positions[3] == 2):
                total += 2
        elif sum(positions) == 3:
            total += 1

    price += total * len(region)

print(price)
