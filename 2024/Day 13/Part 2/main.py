from sympy import solve
from sympy.abc import x, y, z

lines = open('Day 13/Part 1/input.txt').read().splitlines()

tokens_total = 0
for i in range(0, len(lines), 4):
    game = lines[i:i+3]

    _, params_A = game[0].split(':')
    _, params_B = game[1].split(':')

    x1, y1 = params_A.split(',')
    x2, y2 = params_B.split(',')

    x1, y1, x2, y2 = int(x1[2:]), int(y1[2:]), int(x2[2:]), int(y2[2:])

    _, results = game[2].split(':')

    result_x, result_y = results.split(',')
    result_x, result_y = int(
        result_x[3:]) + 10000000000000, int(result_y[3:]) + 10000000000000

    eq1 = x * x1 + y * x2 - result_x
    eq2 = x * y1 + y * y2 - result_y

    solutions = solve([eq1, eq2], (x, y))

    try:
        if solutions and all(sol.is_integer and sol >= 0 for sol in solutions.values()):
            tokens_total += solutions[x] * 3 + solutions[y] * 1
    except Exception:
        continue


print(tokens_total)
