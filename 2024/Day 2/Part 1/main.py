lines = open('Day 2/Part 1/input.txt').read().splitlines()
lines = [line.split() for line in lines]


def check_increase(line):
    previous_num = int(line[0])
    for n in range(1, len(line)):
        l = int(line[n])
        if l > previous_num and abs(previous_num - l) >= 1 and abs(previous_num - l) <= 3:
            previous_num = l
        else:
            return 0

    return 1


def check_decrease(line):
    previous_num = int(line[0])
    for n in range(1, len(line)):
        l = int(line[n])
        if l < previous_num and abs(previous_num - l) >= 1 and abs(previous_num - l) <= 3:
            previous_num = l
        else:
            return 0

    return 1


valid = 0
for line in lines:
    valid += check_increase(line) + check_decrease(line)

print(valid)
