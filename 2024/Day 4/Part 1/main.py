lines = open('Day 4/Part 1/input.txt').read().splitlines()

total = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] != 'X':
            continue

        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                if d_row == 0 and d_col == 0:
                    continue
                if not (0 <= row + d_row * 3 < len(lines) and 0 <= col + d_col * 3 < len(lines[0])):
                    continue

                if lines[row+d_row][col+d_col] == 'M' and lines[row+d_row * 2][col+d_col * 2] == 'A' and lines[row+d_row * 3][col+d_col * 3] == 'S':
                    total += 1

print(total)
