from utils import fetch

input_data = fetch(4)


def split_range(a: str):
    _range = a.split('-')
    _range[0] = int(_range[0])
    _range[1] = int(_range[1])
    _range.sort()
    print(_range)
    return _range


def compare(a, b):
    global redundant_elves
    print('comparing', a, 'and', b)

    a = split_range(a)
    elf1 = list(range(a[0], a[1]))
    elf1.append(a[1])
    if a[0] == a[1]:
        elf1.append(a[0])

    b = split_range(b)
    elf2 = list(range(b[0], b[1]))
    elf2.append(b[1])
    if b[0] == b[1]:
        elf2.append(b[0])

    print('elf1:', elf1)
    print('elf2:', elf2)

    already_counted = False

    if elf1[0] in elf2:
        if elf1[len(elf1)-1] in elf2:
            print('elf 1 is inside elf 2')
            redundant_elves += 1
            already_counted = True
    if elf2[0] in elf1:
        if elf2[len(elf2)-1] in elf1:
            if already_counted != True:
                print('elf 2 is inside elf 1')
                redundant_elves += 1


redundant_elves = 0

for line in input_data:
    line = line.decode("utf-8").strip()
    elf = line.split(',')
    compare(elf[0], elf[1])
    print('')

print(redundant_elves)  # 526
