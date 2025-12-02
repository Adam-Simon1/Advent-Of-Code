ids = open("./Day 2/Part 1/input.txt").read().splitlines()[0].split(',')

sm = 0
for id in ids:
    s, e = id.split('-')
    s, e = int(s), int(e)

    for i in range(s, e+1):
        str_i = str(i)

        for j in range(len(str_i)):
            if str_i[:j] == str_i[j:]:
                sm += i

print(sm)
