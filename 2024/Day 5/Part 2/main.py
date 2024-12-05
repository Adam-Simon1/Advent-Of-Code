lines = open('Day 5/Part 1/input.txt').read().splitlines()

rules = {}

instructions = []
for l, line in enumerate(lines):
    if line == '':
        instructions = lines[l+1:]
        break

    num1, num2 = line.split('|')
    num1, num2 = int(num1), int(num2)

    if num2 in rules:
        rules[num2].append(num1)
    else:
        rules[num2] = [num1]


def order(instruction):
    previous_nums = set()

    for i in range(len(instruction)):
        current = int(instruction[i])

        if current in previous_nums:
            instruction[i], instruction[i-1] = instruction[i-1], instruction[i]

            return order(instruction)

        if current in rules:
            previous_nums.update(rules[int(current)])

    return instruction


wrong = []
for instruction in instructions:
    previous_nums = set()
    instruction = instruction.split(',')

    for num in instruction:
        num = int(num)
        if num in previous_nums:
            wrong.append(instruction)
            break

        if num in rules:
            previous_nums.update(rules[int(num)])


total = 0
for instruction in wrong:
    instruction = order(instruction)

    total += int(instruction[len(instruction) // 2])

print(total)
