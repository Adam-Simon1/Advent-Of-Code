ids = open("./Day 2/Part 1/input.txt").read().splitlines()[0].split(',')

sm = 0
for id in ids:
    s, e = id.split('-')
    s, e = int(s), int(e)

    is_valid = True
    for i in range(s, e+1):
        str_i = str(i)

        length = len(str_i)
        for seq_len in range(1, length//2 + 1):
            if length % seq_len != 0:
                continue

            seq = str_i[:seq_len]
            rep = length // seq_len

            if seq * rep == str_i:
                sm += i
                break

print(sm)
