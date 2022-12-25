from aoc22_util.input import *

def signum(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

def move(new_head, tail):
    delta_x = new_head[0] - tail[0]
    delta_y = new_head[1] - tail[1]
    if abs(delta_x) >= 2 or abs(delta_y) >= 2:
        return (tail[0] + signum(delta_x), tail[1] + signum(delta_y))
    return tail

if __name__ == "__main__":

    visited_p1 = {(0, 0)}
    visited_p2 = {(0, 0)}
    head = (0, 0)
    rope = [(0,0) for _ in range(9)]

    for line in file_readlines_stripped("09/input.txt"):
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            match direction:
                case "U":
                    head = (head[0], head[1] + 1)
                case "D":
                    head = (head[0], head[1] - 1)
                case "R":
                    head = (head[0] + 1, head[1])
                case "L":
                    head = (head[0] - 1, head[1])
                case _:
                    raise Exception(f"Unknown direction '{direction}'")
            prev = head
            for i, _ in enumerate(rope):
                rope[i] = move(prev, rope[i])
                prev = rope[i]
            visited_p1.add(rope[0])
            visited_p2.add(rope[-1])

    print(len(visited_p1), len(visited_p2))
