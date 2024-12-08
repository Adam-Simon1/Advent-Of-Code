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

antinodes = set()
for key in locations:
    for l1 in range(len(locations[key])):
        for l2 in range(l1 + 1, len(locations[key])):
            loc1 = locations[key][l1]
            loc2 = locations[key][l2]

            distance1 = (loc1[0] - loc2[0], loc1[1] - loc2[1])
            distance2 = (loc2[0] - loc1[0], loc2[1] - loc1[1])

            antin_loc1 = tuple(map(operator.add, loc1, distance1))
            antin_loc2 = tuple(map(operator.add, loc2, distance2))

            if 0 <= antin_loc1[0] < len(lines) and 0 <= antin_loc1[1] < len(lines[0]):
                antinodes.add(antin_loc1)

            if 0 <= antin_loc2[0] < len(lines) and 0 <= antin_loc2[1] < len(lines[0]):
                antinodes.add(antin_loc2)

print(len(antinodes))
