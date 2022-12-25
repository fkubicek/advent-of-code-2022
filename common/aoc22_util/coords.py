import math

from numbers import Number
from typing import NamedTuple, Self

class Coords2D(NamedTuple):
    ADJACENT_DIFFS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    DIAGONAL_DIFFS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    ALL_DIFFS = ADJACENT_DIFFS + DIAGONAL_DIFFS

    x: Number
    y: Number

    def adjacent_neighbors(self):
        return [Coords2D(self.x + dx, self.y + dy) for dx, dy in Coords2D.ADJACENT_DIFFS]
    
    def diagonal_neighbors(self):
        return [Coords2D(self.x + dx, self.y + dy) for dx, dy in Coords2D.DIAGONAL_DIFFS]

    def all_neighbors(self):
        return [Coords2D(self.x + dx, self.y + dy) for dx, dy in Coords2D.ALL_DIFFS]

    def manhattan_distance(self, other: Self=None):
        if other is None:
            other = Coords2D(0,0)
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def euclidean_distance(self, other: Self=None):
        if other is None:
            other = Coords2D(0,0)
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __abs__(self):
        return Coords2D(abs(self.x), abs(self.y))
    
    def __add__(self, other: Self):
        return Coords2D(self.x + other.x, self.y + other.y)
    
    def __mul__(self, n) -> Self:
        return Coords2D(self.x * n, self.y * n)
    
    def __rmul__(self, n) -> Self:
        return Coords2D(self.x * n, self.y * n)

    def __repr__(self):
        return f"〈{self.x}, {self.y}〉"

    def __sub__(self, other: Self):
        return Coords2D(self.x - other.x, self.y - other.y)
