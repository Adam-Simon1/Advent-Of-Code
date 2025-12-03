lines = open("./Day 3/Part 1/input.txt").read().splitlines()

sm = 0
for line in lines:
    mx = (0, 0)
    for n in range(len(line) - 1):
        num = int(line[n])

        if num > mx[0]:
            mx = (num, n)

    mx2 = (0, 0)
    for i in range(mx[1]+1, len(line)):
        num = int(line[i])

        if num > mx2[0]:
            mx2 = (num, i)

    final = int(str(mx[0]) + str(mx2[0]))

    sm += final

print(sm)
