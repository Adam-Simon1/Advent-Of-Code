from collections import defaultdict

lines = open('Day 22/Part 1/input.txt').read().splitlines()

total = 0
seqs = defaultdict(int)


def get_secret(sec_num):
    sec_num = int(sec_num)

    new_num = sec_num * 64
    sec_num ^= new_num
    sec_num %= 16777216

    new_num = sec_num // 32
    sec_num ^= new_num
    sec_num %= 16777216

    new_num = sec_num * 2048
    sec_num ^= new_num
    sec_num %= 16777216

    return sec_num


for sec_num in lines:
    sec_num = int(sec_num)
    nums = []

    for _ in range(2000):
        nums.append(sec_num % 10)
        sec_num = get_secret(sec_num)

    changes = []
    for i in range(1, len(nums)):
        changes.append(nums[i] - nums[i-1])

    appeared = set()
    for i in range(len(nums)):
        seq = changes[i:i+4]

        if len(seq) != 4:
            continue

        seq = tuple(seq)
        if seq not in appeared:
            appeared.add(seq)
            seqs[seq] += nums[i+4]

print(max(seqs.values()))
