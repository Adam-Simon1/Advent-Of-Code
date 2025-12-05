lines = open("./Day 5/Part 1/input.txt").read().splitlines()

fresh = []
ids = []
for l in range(len(lines)):
    if lines[l] == '':
        fresh = lines[:l]
        ids = lines[l + 1:]
        break

new_fresh = []
for item in fresh:
    s, e = item.split('-')
    s, e = int(s), int(e)

    new_fresh.append((s, e))

fresh = sorted(new_fresh, key=lambda x: x[0])

last = None
cnt = 0
for s, e in fresh:
    if last is None:
        last = (s, e)
    elif last[1] < s:
        cnt += last[1] - last[0] + 1
        last = (s, e)
    else:
        last = (last[0], max(last[1], e))

cnt += last[1] - last[0] + 1

print(cnt)
