from utils import fetch

input_data = fetch(3)


def char_to_int(char: str):
    number = ord(char)
    if number >= 97:
        number -= 96
    else:
        number -= 64
        number += 26
    return number


def calculate_priority(items: str):
    count = 0
    for item in items:
        count += char_to_int(item)
    return count


def find_in_both(a: str, b: str):
    string = ''
    for char in a:
        if char in list(b):
            string += char
    return dedupe_string(string)


def find_in_all(group_array):
    string = ''
    for char in group_array[0]:
        if char in list(group_array[1]):
            if char in list(group_array[2]):
                string += char

    return dedupe_string(string)


def dedupe_string(string: str):
    return "".join(set(string))


priority_value = 0
badge_value = 0
i = 0
group = ['','','']

for line in input_data:
    i += 1
    line = line.decode("utf-8")
    left_pocket = line[:len(line)//2].strip()
    right_pocket = line[len(line)//2:].strip()

    group[i % 3] = line.strip()
    if i % 3 == 0:
        badge_item = find_in_all(group)
        badge_value += calculate_priority(badge_item)

    priority_items = find_in_both(left_pocket, right_pocket)
    if priority_items != '':
        priority_value += calculate_priority(priority_items)

print(priority_value)
print(badge_value)