import sys

from utils import fetch
import re

input_data = fetch(5)


def move_data(line: str):
    match = re.match('move (\d+) from (\d+) to (\d+)', line)
    _count = int(match.group(1))
    _from = int(match.group(2))-1
    _to = int(match.group(3))-1

    for i in range(_count):
        values_to_move = crate_mover_9000[_from][-1:]
        crate_mover_9000[_to] = crate_mover_9000[_to] + values_to_move
        crate_mover_9000[_from] = crate_mover_9000[_from][:-1]

    values_to_move = crate_mover_9001[_from][-_count:]
    crate_mover_9001[_to] = crate_mover_9001[_to] + values_to_move
    crate_mover_9001[_from] = crate_mover_9001[_from][:-_count]


crate_mover_9000 = [[], [], [], [], [], [], [], [], []]
crate_mover_9001 = [[], [], [], [], [], [], [], [], []]

for line in input_data:
    line = line.decode("utf-8")

    if line.startswith('move'):
        move_data(line)
    elif '[' in line:
        for i, column in enumerate(re.findall('....?', line)):
            char = column.strip('[] ')
            if char != '':
                crate_mover_9000[i].insert(0, char)
                crate_mover_9001[i].insert(0, char)

part1 = ''
part2 = ''
for i, column in enumerate(crate_mover_9000):
    part1 += column[len(column)-1]

for i, column in enumerate(crate_mover_9001):
    part2 += column[len(column)-1]

print(part1)
print(part2)