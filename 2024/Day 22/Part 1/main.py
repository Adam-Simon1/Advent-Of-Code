lines = open('Day 22/Part 1/input.txt').read().splitlines()

total = 0
for sec_num in lines:
    sec_num = int(sec_num)
    for _ in range(2000):
        new_num = sec_num * 64
        sec_num ^= new_num
        sec_num %= 16777216

        new_num = sec_num // 32
        sec_num ^= new_num
        sec_num %= 16777216

        new_num = sec_num * 2048
        sec_num ^= new_num
        sec_num %= 16777216

    total += sec_num

print(total)
