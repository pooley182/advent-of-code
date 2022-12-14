from math import ceil
from utils import fetch

input_lines = fetch(14).read().decode("utf-8").splitlines()

grid = {}

min_x = pow(2, 32)
max_x = 0
min_y = 0
max_y = 0

part_1 = 0
part_2 = 0

grid[(500,0)] = '+'

for line in input_lines:
    location = line.split(' -> ')

    for i in range(len(location)-1):
        x1, y1 = [int(n) for n in location[i].split(',')]
        x2, y2 = [int(n) for n in location[i+1].split(',')]

        max_x = max(max_x, x1, x2)
        min_x = min(min_x, x1, x2)
        max_y = max(max_y, y1, y2)

        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                grid[(x1, j)] = '#'
        else:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                grid[(j, y1)] = '#'

for i in range(max_y+1):
    min_x = 500 - ceil(max_y * 1.1)
    max_x = 500 + ceil(max_y * 1.1)
    for j in range(min_x-1, max_x+2):
        if i == max_y:
            grid[(j, i + 1)] = '.'
            grid[(j, i + 2)] = '#'
        if (j, i) not in grid:
            grid[(j, i)] = '.'


def run():
    global part_1, part_2, grid, max_x, min_x, max_y, min_y

    a = 0
    while True:
        a += 1
        c = (500,0)

        ok = False
        while not ok:
            ok = True

            if part_1 == 0 and c[1] == max_y:
                part_1 = a - 1

            if grid[(c[0], c[1]+1)] == '.':
                ok = False
                c = (c[0], c[1]+1)
            elif grid[(c[0]-1, c[1]+1)] == '.':
                ok = False
                c = (c[0]-1, c[1]+1)
            elif grid[(c[0]+1, c[1]+1)] == '.':
                ok = False
                c = (c[0]+1, c[1]+1)


        if c == (500,0):
            part_2 = a
            return

        grid[(c[0], c[1])] = 'o'


run()

for i in range(max_y+3):
    for j in range(min_x-1, max_x+2):
        print(grid[(j, i)], end='')
    print()

print('part 1:', part_1)
print('part 2:', part_2)