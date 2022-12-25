from aoc22_util.input import *
from aoc22_util.coords import Coords2D

def signum(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

def move(new_head: Coords2D, tail: Coords2D):
    delta_x = new_head.x - tail.x
    delta_y = new_head.y - tail.y
    if abs(delta_x) >= 2 or abs(delta_y) >= 2:
        return tail + Coords2D(signum(delta_x), signum(delta_y))
    return tail

if __name__ == "__main__":

    visited_p1 = {Coords2D(0, 0)}
    visited_p2 = {Coords2D(0, 0)}
    head = Coords2D(0, 0)
    rope = [Coords2D(0,0) for _ in range(9)]

    for line in file_readlines_stripped("09/input.txt"):
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            match direction:
                case "U":
                    head += Coords2D(0, 1)
                case "D":
                    head += Coords2D(0, -1)
                case "R":
                    head += Coords2D(1, 0)
                case "L":
                    head += Coords2D(-1, 0)
                case _:
                    raise Exception(f"Unknown direction '{direction}'")
            prev = head
            for i, _ in enumerate(rope):
                rope[i] = move(prev, rope[i])
                prev = rope[i]
            visited_p1.add(rope[0])
            visited_p2.add(rope[-1])

    print(len(visited_p1), len(visited_p2))
