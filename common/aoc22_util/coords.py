import math

from numbers import Number
from typing import NamedTuple, Self

class Coords2D(NamedTuple("Coords2D", [("x", Number), ("y", Number)])):
    ADJACENT_DIFFS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    DIAGONAL_DIFFS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    ALL_DIFFS = ADJACENT_DIFFS + DIAGONAL_DIFFS

    min_x = None
    max_x = None
    min_y = None
    max_y = None

    def __new__(cls: type[Self], x, y) -> Self:
        if isinstance(x, Number) and isinstance(y, Number):
            return super().__new__(cls, x, y)
        raise TypeError("Coords2D arguments must be numbers.")
    
    @staticmethod
    def make_coords_record_extremes(x: Number, y: Number):
        Coords2D.min_x = x if Coords2D.min_x is None else min(Coords2D.min_x, x)
        Coords2D.max_x = x if Coords2D.max_x is None else max(Coords2D.max_x, x)
        Coords2D.min_y = y if Coords2D.min_y is None else min(Coords2D.min_y, y)
        Coords2D.max_y = y if Coords2D.max_y is None else max(Coords2D.max_y, y)
        return Coords2D(x, y)

    def adjacent_neighbors(self) -> list[Self]:
        return [type(self)(self.x + dx, self.y + dy) for dx, dy in self.ADJACENT_DIFFS]
    
    def diagonal_neighbors(self) -> list[Self]:
        return [type(self)(self.x + dx, self.y + dy) for dx, dy in self.DIAGONAL_DIFFS]

    def all_neighbors(self) -> list[Self]:
        return [type(self)(self.x + dx, self.y + dy) for dx, dy in self.ALL_DIFFS]
    
    def is_in_bounds(self, min_coords: Self, max_coords: Self):
        return (
            min_coords.x <= self.x and self.x <= max_coords.x and
            min_coords.y <= self.y and self.y <= max_coords.y
        )

    def manhattan_distance(self, other: Self=None) -> Number:
        if other is None:
            other = type(self)(0,0)
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def euclidean_distance(self, other: Self=None) -> float:
        if other is None:
            other = type(self)(0,0)
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    @staticmethod
    def _signum_number(x: Number) -> int:
        if x < 0: return -1
        if x > 0: return 1
        return 0

    def signum(self) -> Self:
        return type(self)(self._signum_number(self.x), self._signum_number(self.y))

    def __abs__(self) -> Self:
        return type(self)(abs(self.x), abs(self.y))
    
    def __add__(self, other: Self) -> Self:
        return type(self)(self.x + other.x, self.y + other.y)
    
    def __mul__(self, n) -> Self:
        return type(self)(self.x * n, self.y * n)
    
    def __rmul__(self, n) -> Self:
        return type(self)(self.x * n, self.y * n)

    def __repr__(self) -> str:
        return f"〈{self.x}, {self.y}〉"

    def __sub__(self, other: Self) -> Self:
        return type(self)(self.x - other.x, self.y - other.y)
