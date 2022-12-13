import sys

from utils import fetch

input_data = fetch(12)

input_grid = []
visited = []
distances = {}

max_distance = pow(2, 32)
min_steps_to_start = pow(2, 32)
min_steps_to_a = pow(2, 32)

for line in input_data:
    line = line.decode("utf-8").strip()
    row = [*line]
    input_grid.append(row)

grid_width = len(input_grid[0])
grid_height = len(input_grid)


def find_start():
    r = 0
    c = 0
    global input_grid, distances
    for y in range(len(input_grid)):
        for x in range(len(input_grid[y])):
            distances[(y, x)] = max_distance
            if input_grid[y][x] == 'E':
                distances[(y, x)] = 0
                r = y
                c = x
    return r, c


def directions_can_move(current_position):
    global input_grid, visited
    y = current_position[0]
    x = current_position[1]
    current_elevation = input_grid[y][x]
    if current_elevation == 'E':
        current_elevation = 'z'
    visited.append((y, x))
    directions = []
    if y-1 >= 0:
        up = input_grid[y-1][x]
        if can_move(current_elevation, up, (y-1, x)) and not_visited((y-1, x)):
            directions.append((y-1, x))
    if y < grid_height-1:
        down = input_grid[y+1][x]
        if can_move(current_elevation, down, (y+1, x)) and not_visited((y+1, x)):
            directions.append((y+1, x))
    if x-1 >= 0:
        left = input_grid[y][x-1]
        if can_move(current_elevation, left, (y, x-1)) and not_visited((y, x-1)):
            directions.append((y,x-1))
    if x < grid_width-1:
        right = input_grid[y][x+1]
        if can_move(current_elevation, right, (y, x+1)) and not_visited((y, x+1)):
            directions.append((y,x+1))
    return directions


def can_move(current_elevation, adjacent_elevation, position_tuple):
    global distances, min_steps_to_start, min_steps_to_a
    if adjacent_elevation == 'a':
        min_steps_to_a = min(min_steps_to_a, distances[position_tuple])

    if (current_elevation == 'a' or current_elevation == 'b') and adjacent_elevation == 'S':
        min_steps_to_start = min(min_steps_to_start, distances[position_tuple])
        return True
    elif ord(current_elevation) - 1 <= ord(adjacent_elevation):
        return True
    return False


def not_visited(location):
    global visited
    if location not in visited:
        return True
    return False


def search():
    global distances, visited

    queue = [find_start()]

    while len(queue) > 0:
        current_position = queue.pop(0)

        for next_position in directions_can_move(current_position):
            distances[next_position] = min(distances[next_position], distances[current_position] + 1)
            if not_visited(next_position) and next_position not in queue:
                queue.append(next_position)


search()

print('Minimum distance to endpoint found in', min_steps_to_start, 'steps')

print('Minimum steps from the lowest point found in', min_steps_to_a, 'steps')