import math

from numbers import Number
from typing import NamedTuple, Self

class Coords2D(NamedTuple):
    ADJACENT_DIFFS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    DIAGONAL_DIFFS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    ALL_DIFFS = ADJACENT_DIFFS + DIAGONAL_DIFFS

    x: Number
    y: Number

    def adjacent_neighbors(self) -> list[Self]:
        return [type(self)(self.x + dx, self.y + dy) for dx, dy in self.ADJACENT_DIFFS]
    
    def diagonal_neighbors(self) -> list[Self]:
        return [type(self)(self.x + dx, self.y + dy) for dx, dy in self.DIAGONAL_DIFFS]

    def all_neighbors(self) -> list[Self]:
        return [type(self)(self.x + dx, self.y + dy) for dx, dy in self.ALL_DIFFS]

    def manhattan_distance(self, other: Self=None) -> Number:
        if other is None:
            other = type(self)(0,0)
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def euclidean_distance(self, other: Self=None) -> float:
        if other is None:
            other = type(self)(0,0)
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

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
