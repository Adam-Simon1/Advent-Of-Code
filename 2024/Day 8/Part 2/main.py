import operator

lines = open('Day 8/Part 1/input.txt').read().splitlines()

locations = {}

for row in range(len(lines)):
    for col in range(len(lines[0])):
        char = lines[row][col]
        if char != '.':
            if char in locations:
                locations[char].append((row, col))
            else:
                locations[char] = [(row, col)]


def process(antinodes, loc1, loc2, distance1, distance2):
    rows, cols = len(lines), len(lines[0])

    for k in range(1, max(rows, cols)):
        antin_loc1 = (loc1[0] + k * distance1[0], loc1[1] + k * distance1[1])
        if 0 <= antin_loc1[0] < rows and 0 <= antin_loc1[1] < cols:
            antinodes.add(antin_loc1)

        antin_loc2 = (loc2[0] + k * distance2[0], loc2[1] + k * distance2[1])
        if 0 <= antin_loc2[0] < rows and 0 <= antin_loc2[1] < cols:
            antinodes.add(antin_loc2)


antinodes = set()
for key in locations:
    for l1 in range(len(locations[key])):
        for l2 in range(l1 + 1, len(locations[key])):
            loc1 = locations[key][l1]
            loc2 = locations[key][l2]

            antinodes.add(loc1)
            antinodes.add(loc2)

            distance1 = (loc1[0] - loc2[0], loc1[1] - loc2[1])
            distance2 = (loc2[0] - loc1[0], loc2[1] - loc1[1])

            process(antinodes, loc1, loc2, distance1, distance2)


print(len(antinodes))
