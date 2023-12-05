from utils import fetch

input_data = fetch(4)


def split_string_to_range(a: str):
    _range = a.split('-')
    _range[0] = int(_range[0])
    _range[1] = int(_range[1])
    return _range


def compare_overlap(a: str, b: str):
    global redundant_elves
    global non_overlaps

    a_range = split_string_to_range(a)
    elf1 = set(list(range(a_range[0], a_range[1] + 1)))

    b_range = split_string_to_range(b)
    elf2 = set(list(range(b_range[0], b_range[1] + 1)))

    if elf1.issubset(elf2) or elf2.issubset(elf1):
        redundant_elves += 1

    if not elf1.isdisjoint(elf2):
        non_overlaps += 1


redundant_elves = 0
non_overlaps = 0

for line in input_data:
    line = line.decode("utf-8").strip()
    elf = line.split(',')
    compare_overlap(elf[0], elf[1])

print(redundant_elves)
print(non_overlaps)
