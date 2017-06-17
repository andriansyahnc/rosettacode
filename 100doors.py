import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--doors', type=str,
                        help='How many doors', required=True, default=-1)
    return parser.parse_args()

def doors():
    door = int(get_args().doors)
    door_str = 'closed ' * door
    door_array = (door_str.strip().split(" "))
    i = 1
    while i <= door:
        dome = int(door / i)
        k = 1
        while k <= dome:
            visit = (k * i) - 1
            if visit < door:
                if door_array[visit] == 'closed':
                    door_array[visit] = 'open'
                elif door_array[visit] == 'open':
                    door_array[visit] = 'closed'
            k += 1
        i += 1
    door_idx = 0
    while door_idx < door:
        if door_array[door_idx] == "open":
            print(door_idx + 1)
        door_idx += 1


if __name__ == "__main__":
    doors()
