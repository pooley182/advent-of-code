import re
from utils import fetch

input_lines = fetch(15).read().decode("utf-8").splitlines()

def part_1():
    beacons_y = set()
    ys = set()
    for line in input_lines:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r'-?(\d+)(?=,|:|$)', line))

        if beacon_y == 2000000:
            beacons_y.add(beacon_x)

        d = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        d -= abs(2000000 - sensor_y)
        x = sensor_x
        dx = 0
        for x in range(sensor_x - d, sensor_x + d + 1):
            ys.add(x)

    return len(ys - beacons_y)


def part_2():
    max_x = 4000000
    y_ranges = [[] for _ in range(max_x + 1)]

    for line in input_lines:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r'-?(\d+)(?=,|:|$)', line))

        d = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        dy = 0
        while d > 0:
            x_l = max(0, sensor_x - d)
            x_r = min(max_x, sensor_x + d)
            if sensor_y - dy >= 0:
                y_ranges[sensor_y - dy].append([x_l, x_r])
            if sensor_y + dy <= max_x and dy:
                y_ranges[sensor_y + dy].append([x_l, x_r])
            dy += 1
            d -= 1

    for ans_y in range(max_x + 1):
        xs = y_ranges[ans_y]
        if not xs:
            continue
        xs.sort()

        if xs[0][0] != 0:
            ans_x = 0
            break

        last_e = xs[0][1]
        for i in range(1, len(xs)):
            if last_e >= xs[i][0] - 1:
                last_e = max(last_e, xs[i][1])
            else:
                break

        if last_e != max_x:
            ans_x = last_e + 1
            break

    return max_x * ans_x + ans_y


print('part 1:', part_1())
print('part 2:', part_2())