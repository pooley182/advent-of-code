import time

from utils import fetch

input_data = fetch(10)

commands = []
clock_cycles = 0
x_register = 1
total_signal_strength = 0
row = ''

for line in input_data:
    line = line.decode("utf-8").strip()
    commands.append(line.split(' '))


def tick():
    global clock_cycles
    global total_signal_strength
    global row
    clock_cycles += 1

    sprite_a = x_register - 1
    sprite_b = x_register
    sprite_c = x_register + 1
    pos = (clock_cycles % 40) - 1
    if pos < 0:
        pos = 39
    if pos == sprite_a or pos == sprite_b or pos == sprite_c:
        print('▒▒', end='')
    else:
        print('  ', end='')

    if clock_cycles % 40 == 0:
        print()
        row = ''

    if (clock_cycles - 20) % 40 == 0:
        signal_strength = get_signal_strength()
        total_signal_strength += signal_strength

    time.sleep(.025)


def noop():
    tick()


def addx(value: int):
    global x_register
    tick()
    tick()
    x_register += value


def get_signal_strength():
    global clock_cycles
    global x_register

    return x_register * clock_cycles


for command in commands:
    match command[0]:
        case 'noop':
            noop()
        case 'addx':
            addx(int(command[1]))

print('Signal strength:',total_signal_strength)
