line = open('./Day 11/Part 1/input.txt').read()

line = line.split()

for _ in range(30):
    new_line = []
    for i in range(len(line)):
        num = int(line[i])

        if num == 0:
            new_line.append(1)
        elif len(line[i]) % 2 == 0:
            new_line.append(int(line[i][:len(line[i])//2]))
            new_line.append(int(line[i][len(line[i])//2:]))
        else:
            new_line.append(num * 2024)

    line = [str(x) for x in new_line]

print(len(line))
