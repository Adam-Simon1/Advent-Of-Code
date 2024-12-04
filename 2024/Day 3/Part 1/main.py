import re

lines = open('Day 3/Part 1/input.txt').read()

pattern = r"mul\(\d{1,3},\d{1,3}\)"

matches = re.findall(pattern, lines)

sm = 0
for match in matches:
    nums = re.findall(r"\d{1,3}", match)
    sm += int(nums[0]) * int(nums[1])

print(matches)
