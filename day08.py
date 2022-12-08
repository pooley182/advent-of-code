from utils import fetch

input_data = fetch(8)

input_grid = []
total_visible = 0
most_scenic_score = 0

for line in input_data:
    line = line.decode("utf-8").strip()
    tree_row = [*line]
    input_grid.append(tree_row)

def check_left(x,y) -> bool:
    global input_grid
    visible = True
    scenic_score = 0
    current_height = int(input_grid[y][x])
    for tree in range(x-1, -1, -1):
        scenic_score += 1
        tree_height = int(input_grid[y][tree])
        if tree_height >= current_height:
            visible = False
            break

    return visible, scenic_score


def check_right(x,y) -> bool:
    global input_grid
    visible = True
    scenic_score = 0
    current_height = int(input_grid[y][x])
    for tree in range(x+1, len(input_grid[y]), +1):
        scenic_score += 1
        tree_height = int(input_grid[y][tree])
        if tree_height >= current_height:
            visible = False
            break

    return visible, scenic_score


def check_up(x,y) -> bool:
    global input_grid
    visible = True
    scenic_score = 0
    current_height = int(input_grid[y][x])
    for tree in range(y-1, -1, -1):
        scenic_score += 1
        tree_height = int(input_grid[tree][x])
        if tree_height >= current_height:
            visible = False
            break

    return visible, scenic_score


def check_down(x,y) -> bool:
    global input_grid
    visible = True
    scenic_score = 0
    current_height = int(input_grid[y][x])
    for tree in range(y+1, len(input_grid), +1):
        scenic_score += 1
        tree_height = int(input_grid[tree][x])
        if tree_height >= current_height:
            visible = False
            break

    return visible, scenic_score


for y in range(len(input_grid)):
    for x in range(len(input_grid[y])):
        left = check_left(x, y)
        right = check_right(x, y)
        up = check_up(x, y)
        down = check_down(x, y)
        if left[0] or right[0] or up[0] or down[0]:
            total_visible += 1
        scenic_score = left[1] * right[1] * up[1] * down[1]
        if scenic_score > most_scenic_score:
            most_scenic_score = scenic_score

print(total_visible)
print(most_scenic_score)
