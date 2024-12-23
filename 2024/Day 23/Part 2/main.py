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

        groups.append(([comp, conn], intersect))


def extend_group(group):
    possible = group[1].copy()

    for comp in possible:
        known = group[0]
        intersect = set(known).intersection(set(connections[comp]))

        if len(intersect) != len(known):
            continue

        group[0].append(comp)
        group[1].remove(comp)

    return group


seen = set()
for g, group in enumerate(groups):
    group = extend_group(group)

    combination = frozenset(group[0])
    seen.add(combination)

password = sorted(max(seen, key=len))

print(",".join(password))
