from utils import fetch
import functools

input_data = fetch(13).read().decode("utf-8").splitlines()

indices_in_order = 0
packets = []

def check_order(left, right):
    elements = zip(left, right)
    for a, b in elements:
        if isinstance(a, list) and isinstance(b, list):
            c = check_order(a, b)
            if c == 1 or c == -1:
                return c

        elif isinstance(a, list) and not isinstance(b, list):
            b = [b]
            c = check_order(a, b)
            if c == 1 or c == -1:
                return c

        elif not isinstance(a, list) and isinstance(b, list):
            a = [a]
            c = check_order(a, b)
            if c == 1 or c == -1:
                return c

        else:
            c = compare(a, b)
            if c == 1 or c == -1:
                return c

    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    else:
        return 0


def compare(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    return 0


index = 1
for i in range(0, len(input_data), 3):
    left = eval(input_data[i])
    right = eval(input_data[i+1])
    packets.append(left)
    packets.append(right)

    if check_order(left, right) >= 0:
        indices_in_order += index

    index += 1

packets.append([[2]])
packets.append([[6]])
sorted_packets = sorted(packets, key=functools.cmp_to_key(check_order), reverse = True)
index_left = sorted_packets.index([[2]]) + 1
index_right = sorted_packets.index([[6]]) + 1

print('part 1:',indices_in_order)
print('part 2:',index_left * index_right)