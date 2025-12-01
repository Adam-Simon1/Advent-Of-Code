lines = open("./Day 1/Part 1/input.txt").read().splitlines()

position = 50

cnt = 0
for line in lines:
    for _ in range(int(line[1:])):
        if line[0] == 'R':
            position = (position - 1 + 100) % 100
        else:
            position = (position + 1) % 100

        if position == 0:
            cnt += 1

print(cnt)
