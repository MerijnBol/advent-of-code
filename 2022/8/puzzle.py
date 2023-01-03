import os
import sys
from typing import List

import numpy as np

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_lines(input_filename, dir)


class Map:
    """
    A class for storing a 2d map. The input is a List of horizontal
    rows of the map.
    """

    store: List[int]
    width: int
    height: int

    def __init__(self, itter: List[List[int]]):
        self.width = len(itter[0])
        self.height = len(itter)
        self.store = [0] * (self.width * self.height)
        self._fill_map(itter)

    def get(self, x: int, y: int) -> int:
        return self.store[y * self.width + x]

    def save(self, x: int, y: int, val: int):
        index = y * self.width + x
        self.store[index] = val

    def _fill_map(self, itter: List[List[int]]):
        for y, row in enumerate(itter):
            for x, value in enumerate(row):
                self.save(x, y, int(value))

    @property
    def print_map(self) -> str:
        printlist = np.array_split(self.store, self.height)
        for row in printlist:
            print("".join([str(x) for x in row]))

    def __repr__(self) -> str:
        return f"Map({self.width}x{self.height})"


class PuzzleSolution:
    map: Map

    def __init__(self, data) -> None:
        self._DATA = data
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        self.map = Map(data)

    def is_vissible(self, x: int, y: int) -> bool:
        """Return true if tree vissible from at least on direction."""
        height = self.map.get(x, y)

        # check to left: left border to x.
        if all([self.map.get(dx, y) < height for dx in range(x)]):
            return True

        # check to right: x to right border.
        if all([self.map.get(dx, y) < height for dx in range(x + 1, self.map.width)]):
            return True

        # check to top: top border to y
        if all([self.map.get(x, dy) < height for dy in range(y)]):
            return True

        # check to bottom: y to bottom border
        if all([self.map.get(x, dy) < height for dy in range(y + 1, self.map.height)]):
            return True

        return False

    def get_scenic_score(self, x: int, y: int) -> int:
        if x in [0, self.map.width] or y in [0, self.map.height]:
            # Border trees have a 0 score.
            return 0

        height = self.map.get(x, y)
        # check to left: left border to x.
        left = 0
        for tree in [self.map.get(dx, y) for dx in reversed(range(x))]:
            left += 1
            if tree >= height:
                break

        # check to right: x to right border.
        right = 0
        for tree in [self.map.get(dx, y) for dx in range(x + 1, self.map.width)]:
            right += 1
            if tree >= height:
                break

        # check to top: top border to y
        top = 0
        for tree in [self.map.get(x, dy) for dy in reversed(range(y))]:
            top += 1
            if tree >= height:
                break

        # check to bottom: y to bottom border
        bottom = 0
        for tree in [self.map.get(x, dy) for dy in range(y + 1, self.map.height)]:
            bottom += 1
            if tree >= height:
                break

        return top * right * bottom * left

    def solution_1(self):
        vissible = 0
        for x in range(self.map.width):
            for y in range(self.map.height):
                if self.is_vissible(x, y):
                    vissible += 1
        return vissible

    def solution_2(self):
        self.load_data(self._DATA)  # Reset state.
        max_score = 0
        for x in range(self.map.width):
            for y in range(self.map.height):
                score = self.get_scenic_score(x, y)
                if score > max_score:
                    max_score = score
        return max_score


PuzzleSolution(data)

# The map:
