from itertools import islice
from utils import fetch

input_data = fetch(1)

max_calories = 0
max_elf = 0
calories = 0
elf_count = 1

elf_calories = []

for line in input_data:
    line = line.decode("utf-8")
    if line != '\n':
        calories += int(line)
    else:
        elf_calories.append(calories)
        if calories > max_calories:
            max_calories = calories
            max_elf = elf_count
        calories = 0
        elf_count += 1

print('elf', max_elf, 'is carrying the most calories with', max_calories)

elf_calories.sort(reverse=True)

three_calories = 0
iterator = islice(elf_calories,3)
for cals in iterator:
    three_calories += cals

print('the top 3 elves are carrying a total of', three_calories, 'calories')