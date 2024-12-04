lines = open('Day 1/Part 1/input.txt').read().splitlines()

lines = [line.split() for line in lines]

# Counter
counter = {}
for num in nums:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1
