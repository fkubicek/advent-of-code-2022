import re
from typing import Self

import numpy as np

from aoc22_util.input import *
from aoc22_util.coords import Coords2D

def data_to_string(data):
    int_map = {0: ".", 1: "#", 2: "O"}
    return np.array2string(
        data.T,
        threshold=9999999,
        max_line_width=9999999,
        prefix="",
        suffix="",
        separator="",
        formatter={"int": lambda x: int_map[x]}
    )

if __name__ == "__main__":

    line_pattern = re.compile("(\d+,\d+)")
    rock_segments = []

    for line in file_readlines_stripped("14/input.txt"):
        matches = re.findall(line_pattern, line)
        rock_line = list(map(lambda match: Coords2D.make_coords_record_extremes(*map(int, match.split(","))), matches))
        rock_segments.append(rock_line)

    min_coords_p1 = Coords2D(Coords2D.min_x, 0)
    max_coords_p1 = Coords2D(Coords2D.max_x, Coords2D.max_y)

    height = Coords2D.max_y
    rock_segments.append([
        Coords2D.make_coords_record_extremes(500 - 175, height + 2),
        Coords2D.make_coords_record_extremes(500 + 175, height + 2)
    ])

    min_coords = Coords2D(Coords2D.min_x, 0)
    max_coords = Coords2D(Coords2D.max_x, Coords2D.max_y)

    print(min_coords, max_coords,max_coords - min_coords + Coords2D(1, 1))

    data = np.zeros(max_coords - min_coords + Coords2D(1, 1), dtype=np.int8)

    for rock_line in rock_segments:
        prev = rock_line[0]
        for next in rock_line[1:]:
            direction = (next - prev).signum()
            current = prev
            while current != next:
                data[*(current - min_coords)] = 1
                current += direction
            data[*(current - min_coords)] = 1
            prev = next

    print(data_to_string(data), data.shape, min_coords, max_coords)

    sand_source = Coords2D(500, 0)
    active_sand = sand_source
    total = 0
    steps = 0
    solved_p1 = False
    while active_sand:
        steps += 1
        moved = False
        for delta in [Coords2D(0, 1), Coords2D(-1, 1), Coords2D(1, 1)]:
            potential_pos = active_sand + delta
            if not potential_pos.is_in_bounds(min_coords_p1, max_coords_p1) and not solved_p1:
                print(data_to_string(data), total)
                solved_p1 = True
            if data[*(potential_pos-min_coords)] == 0:
                active_sand = potential_pos
                moved = True
                break
        if not moved:
            data[*(active_sand-min_coords)] = 2
            total += 1
            if active_sand == sand_source:
                break
            active_sand = sand_source
            # print(data_to_string(data), data.shape, min_coords, max_coords)

    print(data_to_string(data), total)
    print("total steps:", steps)
