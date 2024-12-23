lines = open('Day 23/Part 1/input.txt').read().splitlines()

connections = {}
for line in lines:
    a, b = line.split('-')

    if a not in connections:
        connections[a] = []
    if b not in connections:
        connections[b] = []

    connections[a].append(b)
    connections[b].append(a)

groups = []

for comp, conns in connections.items():
    for conn in conns:
        conns2 = connections[conn]
        intersect = set(conns).intersection(set(conns2))

        if len(intersect) == 0:
            continue

        if comp not in conns2:
            continue

        groups.append((comp, conn, intersect))

total = 0
seen = set()
for group in groups:
    for comp3 in group[2]:
        combination = frozenset([group[0], group[1], comp3])

        seen.add(combination)

for group in seen:
    for comp in group:
        if comp.startswith('t'):
            total += 1
            break

print(total)
