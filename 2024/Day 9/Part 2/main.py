line = open('Day 9/Part 1/input.txt').read().strip()

files = {}
blanks = []
index = 0
position = 0

for i in range(len(line)):
    count = int(line[i])

    if i % 2 == 0:
        if count != 0:
            files[index] = (position, count)
            index += 1
    else:
        if count != 0:
            blanks.append((position, count))

    position += count

while index > 0:
    index -= 1
    f_position, f_count = files[index]
    for i, (position, count) in enumerate(blanks):
        if position >= f_position:
            blanks = blanks[:i]
            break

        if f_count <= count:
            if f_count == count:
                blanks.pop(i)
            else:
                blanks[i] = (position + f_count, count - f_count)

            files[index] = (position, f_count)
            break

total = 0
for key, (position, count) in files.items():
    for i in range(position, position + count):
        total += key * i

print(total)
