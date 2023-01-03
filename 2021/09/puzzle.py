import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

map_rows = [[int(x) for x in row] for row in files.read_lines("input.txt", dir)]


class Map:
    """
    A class for storing a 2d map. The input is a List of horizontal
    rows of the map.
    """

    store: List
    width: int
    height: int

    def __init__(self, itter: List[List[int]]):
        self.width = len(itter[0])
        self.height = len(itter)
        self.store = ["x"] * (self.width * self.height)
        self._fill_map(itter)

    def get(self, x: int, y: int) -> Optional[int]:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.store[y * self.width + x]

    def save(self, x: int, y: int, val: int = 1):
        index = y * self.width + x
        self.store[index] = val

    def _fill_map(self, itter: List[List[int]]):
        for y, row in enumerate(itter):
            for x, value in enumerate(row):
                self.save(x, y, value)

    def neighbours(self, x, y) -> List[Tuple[int, int, int]]:
        close = []
        close.append((self.get(x - 1, y), x - 1, y))
        close.append((self.get(x + 1, y), x + 1, y))
        close.append((self.get(x, y - 1), x, y - 1))
        close.append((self.get(x, y + 1), x, y + 1))
        return [x for x in close if x[0] is not None]

    @property
    def low_points(self) -> List[Tuple[int, int, int]]:
        low = []
        for x in range(self.width):
            for y in range(self.height):
                height = self.get(x, y)
                assert height is not None
                if all([height < c[0] for c in self.neighbours(x, y)]):
                    low.append((height, x, y))
        return low

    @property
    def print_map(self):
        printlist = np.array_split(self.store, self.height)
        for row in printlist:
            print("".join([str(x) for x in row]))

    def get_basin(self, low: Tuple[int, int, int]) -> int:
        # in_basin doesn't hold any usefull values. Just using the keys to store
        # all points that are already known to be in basin.
        in_basin = {}
        in_basin[low] = True
        ring: List[Tuple[int, int, int]] = []
        for point in self.neighbours(low[1], low[2]):
            if point[0] < 9:
                ring.append(point)
                in_basin[point] = True
        # At this point the 'ring' var is filled with all the neighbours of the low
        # point. Now let's go outwards untill no low points left.
        while len(ring) > 0:
            temp_ring = []
            for point in ring:
                for n in self.neighbours(point[1], point[2]):
                    if n[0] < 9 and n not in in_basin:
                        temp_ring.append(n)
                        in_basin[n] = True
            ring = temp_ring

        return len(in_basin)


map = Map(map_rows)

# puzzle 1

print(
    f"""
    Puzzle number 1:
    Total risk factor is {sum([1 + x[0] for x in map.low_points])}
    """
)

# puzzle 2
basins = [map.get_basin(point) for point in map.low_points]
basins.sort(reverse=True)

print(
    f"""
    Puzzle number 2:
    The top 3 basin product is {basins[0] * basins[1] * basins[2]}
    """
)
