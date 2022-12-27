import numpy as np

from aoc22_util.input import *
from aoc22_util.coords import Coords2D
from aoc22_util.a_star import *

class Coords(Coords2D, AStarConfiguration):
    start = None
    goal = None
    data = []

    def __hash__(self) -> int:
        return super(Coords2D, self).__hash__()

    def __eq__(self, __o: object) -> bool:
        return super(Coords2D, self).__eq__(__o)

    def h(self) -> Number:
        return self.manhattan_distance(self.goal)

    def neighbors(self) -> list[tuple[Self, int]]:
        return [(n, 1) for n in filter(lambda neighbor: (
            0 <= neighbor.x and neighbor.x < self.data.shape[0] and
            0 <= neighbor.y and neighbor.y < self.data.shape[1] and
            neighbor.height() <= self.height() + 1),
            self.adjacent_neighbors())]

    def is_goal(self) -> bool:
        return self == self.goal
    
    def height(self):
        char = self.data[*self]
        match char:
            case "S": return ord("a")
            case "E": return ord("z")
            case _: return ord(char)


if __name__ == "__main__":
    
    for line in file_readlines_stripped("12/input.txt"):
        line_data = []
        for char in line:
            if char == "S":
                Coords.start = Coords(len(Coords.data), len(line_data))
            elif char == "E":
                Coords.goal = Coords(len(Coords.data), len(line_data))
            line_data.append(char)
        Coords.data.append(line_data)
    Coords.data = np.array(Coords.data)

    res = a_star(Coords.start)
    print(len(res) - 1)

    path_lenghts = []
    for x in range(Coords.data.shape[0]):
        for y in range(Coords.data.shape[1]):
            coords = Coords(x, y)
            if coords.height() == ord("a"):
                res = a_star(coords)
                if res:
                    path_lenghts.append(len(res) - 1)
    path_lenghts.sort()

    print(path_lenghts)
