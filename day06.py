import sys
from utils import fetch

input_data = fetch(6)


def check_chars(string: str, num: int, iteration=0):
    chars_to_check = string[0:num]
    unique_chars = len(set(chars_to_check))

    if unique_chars == num:
        return iteration + unique_chars
    else:
        shorter_string = string[1:]
        return check_chars(shorter_string, num, iteration+1)


for line in input_data:
    line = line.decode("utf-8")
    sys.setrecursionlimit(len(line))

    start_of_packet_index = check_chars(line, 4)
    start_of_message_index = check_chars(line, 14)


print(start_of_packet_index)
print(start_of_message_index)