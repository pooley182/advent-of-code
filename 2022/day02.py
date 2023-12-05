from utils import fetch

input_data = fetch(2)

count = 0
count_2 = 0

def RPS(hand: str, wld: str):
    global count
    if wld == 'W':
        count += 6
    if wld == 'D':
        count += 3

    if hand == 'R':
        count += 1
    if hand == 'P':
        count += 2
    if hand == 'S':
        count += 3

def RPS_2(hand: str, wld: str):
    global count_2
    if wld == 'W':
        count_2 += 6
    if wld == 'D':
        count_2 += 3

    if hand == 'R':
        count_2 += 1
    if hand == 'P':
        count_2 += 2
    if hand == 'S':
        count_2 += 3

for line in input_data:
    line = line.decode("utf-8")
    parts = line.split()

    if parts[0] == 'A':  # Rock
        if parts[1] == 'X':
            RPS('R', 'D')
            RPS_2('S', 'L')
        if parts[1] == 'Y':
            RPS('P', 'W')
            RPS_2('R', 'D')
        if parts[1] == 'Z':
            RPS('S', 'L')
            RPS_2('P', 'W')
    if parts[0] == 'B':  # Paper
        if parts[1] == 'X':
            RPS('R', 'L')
            RPS_2('R', 'L')
        if parts[1] == 'Y':
            RPS('P', 'D')
            RPS_2('P', 'D')
        if parts[1] == 'Z':
            RPS('S', 'W')
            RPS_2('S', 'W')
    if parts[0] == 'C':  # Scissors
        if parts[1] == 'X':
            RPS('R', 'W')
            RPS_2('P', 'L')
        if parts[1] == 'Y':
            RPS('P', 'L')
            RPS_2('S', 'D')
        if parts[1] == 'Z':
            RPS('S', 'D')
            RPS_2('R', 'W')

print(count)
print(count_2)