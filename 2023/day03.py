import re
from collections import defaultdict
from utils import fetch

input_data = list(fetch(3))

symbols = dict()
for y, line in enumerate(input_data):
    line = line.decode("utf-8").strip()
    for x, char in enumerate(line):
        if char not in "1234567890.":
            symbols[(x, y)] = char

part_1_total = 0

gears = defaultdict(list)

for y, line in enumerate(input_data):
    line = line.decode("utf-8").strip()
    for match in re.finditer(r"\d+", line):
        for (symbol_x, symbol_y), char in symbols.items():
            if (match.start() - 1 <= symbol_x <= match.end()) and (y - 1 <= symbol_y <= y + 1):
                number = int(match.group())
                part_1_total += number
                if char == "*":
                    gears[(symbol_x, symbol_y)].append(number)

print('part 1 =', part_1_total)

part_2_total = 0
for gear in gears.values():
    if len(gear) == 2:
        part_2_total += gear[0] * gear[1]

print('part 2 =', part_2_total)
