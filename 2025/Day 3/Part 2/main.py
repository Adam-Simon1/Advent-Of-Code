lines = open("./Day 3/Part 1/input.txt").read().splitlines()


def check(line, x, y, correct=None):
    if correct is None:
        correct = []

    mx = (0, 0)
    for n in range(x, y):
        num = int(line[n])

        if num > mx[0]:
            mx = (num, n)

    correct.append(mx[0])

    if len(correct) == 12:
        return correct

    return check(line, mx[1] + 1, y + 1, correct)


sm = 0
for line in lines:
    num = check(line, 0, len(line) - 11)

    sm += int("".join([str(x) for x in num]))

print(sm)
