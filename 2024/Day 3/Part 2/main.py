import re

lines = open('Day 3/Part 1/input.txt').read()

pattern = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"

matches = re.findall(pattern, lines)

sm = 0
condition = True
for match in matches:
    if re.search(r"do\(\)", match):
        condition = True
    elif re.search(r"don't\(\)", match):
        condition = False
    elif condition:
        nums = re.findall(r"\d{1,3}", match)
        sm += int(nums[0]) * int(nums[1])

print(sm)
