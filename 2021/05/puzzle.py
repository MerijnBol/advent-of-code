import os
import sys
from typing import List, Tuple

import numpy as np

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

coor = [
    [tuple((int(v) for v in c.split(","))) for c in x.split(" -> ")]
    for x in files.read_lines("input.txt", dir)
]


class Map:
    store: List
    width: int
    height: int

    def __init__(self, itter: List[List[Tuple[int, int]]]):
        self.width = 0
        self.height = 0
        for c1, c2 in itter:
            if max(c1[0], c2[0]) > self.width:
                self.width = max(c1[0], c2[0])
            if max(c1[1], c2[1]) > self.height:
                self.height = max(c1[1], c2[1])
        self.width += 1
        self.height += 1
        self.store = [0] * (self.width * self.height)
        self._fill_map(itter)

    def get(self, x: int, y: int) -> int:
        return self.store[y * self.width + x]

    def update(self, x: int, y: int, val: int = 1):
        index = y * self.width + x
        self.store[index] = self.store[index] + val

    def _fill_map(self, itter: List[List[Tuple[int, int]]]):
        for c1, c2 in itter:
            mx = min(c1[0], c2[0])
            dx = max(c1[0], c2[0]) - mx
            my = min(c1[1], c2[1])
            dy = max(c1[1], c2[1]) - my
            # horizontal lines
            if dx == 0:
                for y in range(my, my + dy + 1):
                    self.update(mx, y)
            # vertical lines
            elif dy == 0:
                for x in range(mx, mx + dx + 1):
                    self.update(x, my)
            # diagonal lines
            else:
                assert dx == dy
                x = mx
                y = my
                # Check in what direction diagonals actually run
                if c1[0] < c2[0]:
                    x = mx
                    xstep = 1
                else:
                    x = mx + dx
                    xstep = -1

                if c1[1] < c2[1]:
                    y = my
                    ystep = 1
                else:
                    y = my + dy
                    ystep = -1

                total_steps = dx
                steps = 0

                while steps <= total_steps:
                    self.update(x, y)
                    x += xstep
                    y += ystep
                    steps += 1

    @property
    def overlapping(self) -> int:
        overlap = 0
        for x in self.store:
            if x > 1:
                overlap += 1
        return overlap

    def print_map(self):
        printlist = np.array_split(map.store, map.height)
        for row in printlist:
            print("".join([str(x) for x in row]))


# puzzle 1
straight = [x for x in coor if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
map = Map(straight)

print(
    f"""
    Puzzle number 1:
    Total amount of intersections is {map.overlapping}
    """
)

# puzzle 2
map = Map(coor)

print(
    f"""
    Puzzle number 2:
    Total amount of intersections is {map.overlapping}
    """
)
