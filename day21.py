import re
import operator
from utils import fetch

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

input_data = fetch(21).read().decode("utf-8").splitlines()

def process_input(input_lines):
    m_processed = {}
    m_to_process = {}
    for line in input_lines:
        m, value = re.match('([a-z]{4}): (.*)', line).groups()

        if value.isnumeric():
            m_processed[m] = int(value)
        else:
            m_to_process[m] = value

    return m_processed, m_to_process

def process_operation(o):
    return re.match('([a-z]{4}) ([+*\-/]) ([a-z]{4})', o).groups()

monkeys_processed, monkeys_to_process  = process_input(input_data)

while len(monkeys_to_process) > 0:
    for monkey in list(monkeys_to_process):
        operation = monkeys_to_process[monkey]
        a, operator, b = process_operation(operation)

        if a in monkeys_processed and b in monkeys_processed:
            monkeys_processed[monkey] = int(ops[operator](monkeys_processed[a],monkeys_processed[b]))
            if monkey == "root":
                print("part 1:",monkeys_processed[monkey])
            del monkeys_to_process[monkey]
