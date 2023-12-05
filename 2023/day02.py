import re
from utils import fetch

input_data = fetch(2)

max_red = 12
max_green = 13
max_blue = 14

part_1_total = 0
part_2_total = 0

for line in input_data:
    line = line.decode("utf-8").strip()
    game_id = int(re.sub("Game ", "", line.split(':')[0]))
    game_data = line.split(':')[1].split(';')
    game_success = True
    game_max_red = 0
    game_max_green = 0
    game_max_blue = 0
    for i, game in enumerate(game_data):
        game_round = game.split(',')
        for j, cubes in enumerate(game_round):
            cube = cubes.strip().split(' ')
            k = int(cube[0])
            colour = cube[1]
            if colour == 'red':
                game_max_red = max(game_max_red, k)
                if k > max_red:
                    game_success = False
            elif colour == 'green':
                game_max_green = max(game_max_green, k)
                if k > max_green:
                    game_success = False
            elif colour == 'blue':
                game_max_blue = max(game_max_blue, k)
                if k > max_blue:
                    game_success = False

    if game_success:
        part_1_total += game_id

    game_power = game_max_red * game_max_green * game_max_blue
    part_2_total += game_power


print('part 1 =', part_1_total)
print('part 2 =', part_2_total)
