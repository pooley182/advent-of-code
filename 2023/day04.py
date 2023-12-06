import re
from collections import defaultdict
from utils import fetch

input_data = fetch(4)

part_1_total = 0
part_2_count = defaultdict(int)

for i, line in enumerate(input_data):
    part_2_count[i] += 1
    line = line.decode("utf-8").strip()

    winning_numbers = re.findall(r"\d+", line.split(":")[1].split("|")[0])
    my_numbers = re.findall(r"\d+", line.split(":")[1].split("|")[1])
    val = len(set(winning_numbers) & set(my_numbers))
    if val > 0:
        part_1_total += 2**(val-1)
        for x in range(val):
            part_2_count[i+1+x] += part_2_count[i]


print('part 1 =', part_1_total)
print('part 2 =', sum(part_2_count.values()))
