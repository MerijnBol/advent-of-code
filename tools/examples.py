from typing import Any, Dict, List, Tuple

import numpy as np


class Map:
    """
    A class for storing a 2d map. The input is a List of horizontal
    rows of the map.
    """

    store: List[str]
    width: int
    height: int

    def __init__(self, itter: List[List[Any]]):
        self.width = len(itter[0])
        self.height = len(itter)
        self.store = ["x"] * (self.width * self.height)
        self._fill_map(itter)

    def get(self, x: int, y: int) -> Any:
        return self.store[y * self.width + x]

    def save(self, x: int, y: int, val: Any):
        index = y * self.width + x
        self.store[index] = val

    def _fill_map(self, itter: List[List[Any]]):
        for y, row in enumerate(itter):
            for x, value in enumerate(row):
                self.save(x, y, value)

    @property
    def print_map(self) -> str:
        printlist = np.array_split(self.store, self.height)
        for row in printlist:
            print("".join([str(x) for x in row]))

    def __repr__(self) -> str:
        return f"Map({self.width}x{self.height})"
