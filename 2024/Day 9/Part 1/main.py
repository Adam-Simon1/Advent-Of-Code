line = open('Day 9/Part 1/input.txt').read().strip()

disk = []
disk_no_spaces = []
index = 0
for j in range(len(line)):
    if j % 2 == 0:
        disk += [index] * int(line[j])
        disk_no_spaces += [index] * int(line[j])
        index += 1
    else:
        if '.' * int(line[j]) != '':
            disk += [-1] * int(line[j])

new_disk = []
for i in range(len(disk_no_spaces)):
    curr = disk[i]

    if curr == -1:
        new_disk.append(disk_no_spaces[-1])
        disk_no_spaces = disk_no_spaces[:-1]
    else:
        new_disk.append(curr)


total = 0
for n, num in enumerate(new_disk):
    total += int(num) * n

print(total)
