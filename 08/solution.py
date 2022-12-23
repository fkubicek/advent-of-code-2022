import numpy as np

from aoc22_util.input import *

def parse_input(input_path):
    lines = list(map(lambda line: list(map(int, line)), file_readlines_stripped(input_path)))
    lines = np.array(lines)
    print(lines)
    return lines

def is_valid_coords(data, coords):
    return (coords[0] < data.shape[0] and coords[1] < data.shape[1] and coords[0] >= 0 and coords[1] >= 0)

def mark_visible(data, visible, coords, direction):
    highest = -1
    while is_valid_coords(data, coords):
        if data[*coords] > highest:
            visible[*coords] = True
            highest = data[*coords]
        coords += direction

def mark_viewing_distance(data, scenic_scores, coords):
    total = 1
    height = data[*coords]
    for direction in [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]:
        direction_total = 0
        direction_coords = coords.copy()
        while True:
            direction_coords += direction
            if not is_valid_coords(data, direction_coords):
                break
            direction_total += 1
            if data[*direction_coords] >= height:
                break
        total *= direction_total
    scenic_scores[*coords] = total

def part_one(data):
    visible = np.zeros(data.shape, dtype=np.bool8)

    for x in range(data.shape[0]):
        mark_visible(data, visible, np.array([x, 0]), np.array([0, 1]))
        mark_visible(data, visible, np.array([x, data.shape[1] - 1]), np.array([0, -1]))

    for y in range(data.shape[1]):
        mark_visible(data, visible, np.array([0, y]), np.array([1, 0]))
        mark_visible(data, visible, np.array([data.shape[0] - 1, y]), np.array([-1, 0]))

    print(visible)
    print(visible.sum())

def part_two(data):
    scenic_scores = np.zeros(data.shape, dtype=np.int32)
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            mark_viewing_distance(data, scenic_scores, np.array([x, y]))
    print(scenic_scores)
    print(scenic_scores.max())


if __name__ == "__main__":
    data = parse_input("08/input.txt")
    part_one(data)
    part_two(data)
