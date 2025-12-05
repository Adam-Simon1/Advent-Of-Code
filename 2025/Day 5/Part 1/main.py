lines = open("./Day 5/Part 1/input.txt").read().splitlines()

fresh = []
ids = []
for l in range(len(lines)):
    if lines[l] == '':
        fresh = lines[:l]
        ids = lines[l + 1:]
        break

cnt = 0
for item in ids:
    item = int(item)

    for rng in fresh:
        s, e = rng.split('-')
        s, e = int(s), int(e)

        if item in range(s, e+1):
            cnt += 1
            break

print(cnt)
