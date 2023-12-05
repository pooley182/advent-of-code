import math

from utils import fetch

input_data = fetch(11).read().decode("utf-8").splitlines()
monkeys = []


for i in range(0, len(input_data), 7):
    starting_items = input_data[i+1].split(':')[1].strip()
    monkeys.append({
        'items': list(map(int, starting_items.split(','))),
        'operation': input_data[i+2].split('=')[1].strip(),
        'test_number': int(input_data[i+3].split()[-1]),
        'true': int(input_data[i+4].split()[-1]),
        'false': int(input_data[i+5].split()[-1])
    })


def rounds(count, worry_divisor):
    global monkeys
    inspected = [0]*len(monkeys)
    least_common_multiple = math.lcm(*map(lambda m: m['test_number'], monkeys))
    monkey_items = [monkey['items'][:] for monkey in monkeys]
    for a in range(count):
        for b, monkey in enumerate(monkeys):
            while monkey_items[b]:
                item = monkey_items[b].pop()
                operation = monkey['operation'].replace('old', str(item))
                value = eval(operation) // worry_divisor
                target_monkey = monkey['true'] if value % monkey['test_number'] == 0 else monkey['false']
                monkey_items[target_monkey].append(value if worry_divisor != 1 else value % least_common_multiple)
                inspected[b] += 1

    inspected.sort()
    return inspected[-1] * inspected[-2]


part1 = rounds(20, 3)
part2 = rounds(10000, 1)

print('Part 1:', part1)
print('Part 2:', part2)