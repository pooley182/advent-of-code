import re
from utils import fetch

input_data = fetch(1)


def strip_non_numeric(s: str, replace_words=False):
    if replace_words:
        s = re.sub("one", "o1e", s)
        s = re.sub("two", "t2o", s)
        s = re.sub("three", "t3e", s)
        s = re.sub("four", "f4r", s)
        s = re.sub("five", "f5e", s)
        s = re.sub("six", "s6x", s)
        s = re.sub("seven", "s7n", s)
        s = re.sub("eight", "e8t", s)
        s = re.sub("nine", "n9e", s)
    s = re.sub("[^0-9]", "", s)
    return s


def find_left_int(s: str, replace_words=False):
    return strip_non_numeric(s, replace_words)[0]


def find_right_int(s: str, replace_words=False):
    clean = strip_non_numeric(s, replace_words)
    return clean[len(clean)-1]


part_1_total = 0
part_2_total = 0

for line in input_data:
    line = line.decode("utf-8").strip()
    a = find_left_int(line)
    b = find_right_int(line)
    c = find_left_int(line, True)
    d = find_right_int(line, True)

    i = int(a+b)
    j = int(c+d)

    part_1_total += i
    part_2_total += j

print('part 1 =', part_1_total)
print('part 2 =', part_2_total)
