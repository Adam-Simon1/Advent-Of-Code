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

total = 0
for instruction in instructions:
    previous_nums = set()
    instruction = instruction.split(',')
    valid = True

    for num in instruction:
        num = int(num)
        if num in previous_nums:
            valid = False
            break

        if num in rules:
            previous_nums.update(rules[int(num)])

    if valid:
        total += int(instruction[len(instruction)//2])


