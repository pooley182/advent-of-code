from utils import fetch

input_data = fetch(9)

steps = []
visited = set()

for line in input_data:
    line = line.decode("utf-8").strip()
    steps.append(line.split(' '))


def tail_coords_visited(tail_length: int):
    global steps

    head_position = (0, 0)
    tail_positions = []
    for i in range(tail_length):
        tail_positions.append((0, 0))

    visited.add(head_position)

    for direction, count in steps:
        for i in range(int(count)):
            match direction:
                case 'U':
                    x = 0
                    y = 1
                case 'D':
                    x = 0
                    y = -1
                case 'L':
                    x = -1
                    y = 0
                case 'R':
                    x = 1
                    y = 0

            head_position = move(head_position, x, y)
            # print('moving head to position', head_position)
            tail_positions[0] = drag(head_position, tail_positions[0])
            for j in range(1, len(tail_positions)):
                tail_positions[j] = drag(tail_positions[j-1], tail_positions[j])

            # 'visited' is a set so all values will be distinct, we don't have to check if we already have it.
            visited.add(tail_positions[len(tail_positions) - 1])


def move(position, x, y):
    return position[0] + x, position[1] + y


def drag(head_position, tail_position):
    if head_position == tail_position or (abs(tail_position[0] - head_position[0]) < 2 and abs(tail_position[1] - head_position[1]) < 2):
        return tail_position

    if tail_position[0] == head_position[0]:
        new_x = tail_position[0]
    elif head_position[0] - tail_position[0] > 0:
        new_x = tail_position[0] + 1
    else:
        new_x = tail_position[0] - 1

    if tail_position[1] == head_position[1]:
        new_y = tail_position[1]
    elif head_position[1] - tail_position[1] > 0:
        new_y = tail_position[1] + 1
    else:
        new_y = tail_position[1] - 1

    # print('dragging tail to position', (new_x, new_y))
    return new_x, new_y


tail_coords_visited(1)
print('part1:', len(visited))

visited.clear()
tail_coords_visited(9)
print('part2:', len(visited))
