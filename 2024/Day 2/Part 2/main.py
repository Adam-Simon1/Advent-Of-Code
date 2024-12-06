lines = open('Day 2/Part 1/input.txt').read().splitlines()
lines = [line.split() for line in lines]


def check_increase(line, problem=0):
    for n in range(len(line)):

        if n < len(line) - 1:
            next_num = int(line[n+1])
        else:
            break

        l = int(line[n])
        if l < next_num and abs(next_num - l) >= 1 and abs(next_num - l) <= 3:
            pass
        else:
            problem += 1

            if problem > 1:
                return 0

            del line[n]
            return check_increase(line, problem)

    return 1 if problem <= 1 else 0


def check_decrease(line, problem=0):
    for n in range(len(line)):

        if n < len(line) - 1:
            next_num = int(line[n+1])
        else:
            break

        l = int(line[n])
        if l > next_num and abs(next_num - l) >= 1 and abs(next_num - l) <= 3:
            pass
        else:
            problem += 1

            if problem > 1:
                return 0

            del line[n]
            return check_decrease(line, problem)

    return 1 if problem <= 1 else 0


valid = 0
for line in lines:
    valid += check_decrease(line)
    valid += check_increase(line)

print(valid)
