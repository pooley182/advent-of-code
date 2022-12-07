from utils import fetch
import os
import subprocess

input_data = fetch(7)
root_dir = subprocess.check_output(['pwd']).decode("utf8").strip() + '/day7'


def build_folder_structure(input_data):
    global root_dir
    try:
        os.mkdir(root_dir)
    except OSError:
        os.system('rm -rf ' + root_dir)
        os.mkdir(root_dir)

    working_dir = root_dir

    for line in input_data:
        line = line.decode("utf-8").strip()
        if line.startswith('$ cd '):
            if line == '$ cd /':
                working_dir = root_dir
            elif '..' in line:
                working_dir = working_dir[:working_dir.rfind('/')]
            else:
                directory_name = line[5:]
                working_dir += '/' + directory_name
        if line.startswith('dir '):
            directory_name = line[4:]
            os.system('mkdir ' + working_dir + '/' + directory_name)
        if line[0].isdigit():
            file_size, file_name = line.split(' ')
            with open(working_dir + '/' + file_name, 'w') as f:
                for i in range(int(file_size)):
                    f.write('a')


part_1 = 0
part_2 = 70000000

total_used_space = 0
file_system_size = 70000000
update_size = 30000000


def get_size(directory_path, free_space_needed=0):
    global part_1
    global part_2
    for dirpath, dirnames, filenames in os.walk(directory_path):
        sub_dir_size = 0
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            s = get_size(dp, free_space_needed)
            sub_dir_size += s
            # print('checking directory', dp, '=', s)
        directory_size = 0
        for f in filenames:
            fp = os.path.join(dirpath, f)
            directory_size += os.path.getsize(fp)
            # print('checking file', fp, '=', directory_size)

        size = (directory_size + sub_dir_size)
        if size <= 100000:
            part_1 += (directory_size + sub_dir_size)
        if free_space_needed > 0:
            if size > free_space_needed and size < part_2:
                part_2 = size

        break

    return (directory_size + sub_dir_size)


def clean_up():
    global root_dir
    os.system('rm -rf ' + root_dir)


build_folder_structure(input_data)
total_used_space = get_size(root_dir)
print('Total used space:', total_used_space)
free_space_needed = update_size - (file_system_size - total_used_space)
print('Part 1:', part_1)
print('Free space needed:', free_space_needed)
get_size(root_dir, free_space_needed)
print('Part 2:', part_2)
clean_up()
