from typing import Self
from numbers import Number
import math

import heapy

class AStarConfiguration:

    def __hash__(self) -> int:
        raise NotImplementedError

    def __eq__(self, __o: object) -> bool:
        raise NotImplementedError

    def h(self) -> Number:
        raise NotImplementedError

    def neighbors(self) -> list[tuple[Self, int]]:
        """Returns a list of all neighbors with the costs of the edges between this configuration and the respective neighbors."""
        raise NotImplementedError

    def is_goal(self) -> bool:
        raise NotImplementedError


class AStarConfiguration2D(AStarConfiguration):
    """AStarConfiguration characterized by X and Y coordinates."""

    ADJACENT_DIFFS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DIAGONAL_DIFFS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    ALL_DIFFS = ADJACENT_DIFFS + DIAGONAL_DIFFS

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __key(self):
        return (self.x, self.y)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, __o: object) -> bool:
        if (isinstance(__o, AStarConfiguration2D)):
            return self.__key() == __o.__key()
        return False

    def manhattan_distance(self, other: Self):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def euclidean_distance(self, other: Self):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


def reconstruct_path(prev, current):
    path = []
    while current:
        path.append(current)
        current = prev.get(current) # returns None if key not in dict
    path.reverse()
    return path

def a_star(start: AStarConfiguration):
    generator = __a_star_impl(start)
    try:
        queue_inserts, current, neighbors_nodes_only = generator.__next__()
    except StopIteration as e:
        return e.value

def a_star_generator(start: AStarConfiguration):
    return __a_star_impl(start, True)

def __a_star_impl(start: AStarConfiguration, generator=False):
  
    prev = {}
    g_score = {}
    g_score[start] = 0
    pq = heapy.pqueue()
    pq[start] = start.h()

    if generator:
        queue_inserts = []

    while pq:
        current: AStarConfiguration = pq.pop()[0]
        if current.is_goal():
            if generator:
                yield queue_inserts, current, []
            return reconstruct_path(prev, current)

        neighbors = current.neighbors()
        neighbors_nodes_only = [n[0] for n in neighbors]

        if generator:
            yield queue_inserts, current, neighbors_nodes_only
            queue_inserts.clear()

        for neighbor, edge_cost in neighbors:
            new_g_score = g_score[current] + edge_cost
            if new_g_score < g_score.get(neighbor, math.inf):
                prev[neighbor] = current
                g_score[neighbor] = new_g_score
                f = new_g_score + neighbor.h()
                pq[neighbor] = f

                if generator:
                    queue_inserts.append((neighbor, f))

    return None
