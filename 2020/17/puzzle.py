import os
import sys
from collections import defaultdict
from copy import deepcopy
from typing import Dict, List, Tuple

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

data = files.read_lines("test.txt", dir)


class Pocket:
    """
    Pocket is the main dict.
    During cycle operation:
    Frozen is used for the cycle querry loop. Nothing may operate on frozen
    to prevent RuntimeErrors.
    """

    dimensions: int
    pocket: defaultdict[int, defaultdict[int, defaultdict[int, bool]]]

    def __init__(self, plane: List[str], dimensions: int):
        self.dimensions = dimensions
        self.pocket = defaultdict(self._y_values)
        for y, line in enumerate(plane):
            for x, state in enumerate(line):
                self.pocket[x][y][0] = True if state == "#" else False
        frozen = deepcopy(self.pocket)
        # expand borders. Everytime we get a value from the default dicts,
        # that value then 'exists'.
        for x, yz in frozen.items():
            for y, zplane in yz.items():
                for z in zplane.keys():
                    self._get_neighbours(x, y, z, self.pocket)

    def cycle(self):
        frozen = deepcopy(self.pocket)
        # expand borders:
        for x, yz in frozen.items():
            for y, zplane in yz.items():
                for z in zplane.keys():
                    self._get_neighbours(x, y, z, self.pocket)

        frozen = deepcopy(self.pocket)
        frozen2 = deepcopy(self.pocket)
        for x, yz in frozen.items():
            for y, zplane in yz.items():
                for z, value in zplane.items():
                    prox = self._get_neighbours(x, y, z, frozen2)
                    self.pocket[x][y][z] = self._switch(value, prox)

    @property
    def active(self) -> int:
        total = 0
        for yz in self.pocket.values():
            for zplane in yz.values():
                total += [x for x in zplane.values()].count(True)
        return total

    @property
    def z0(self):
        "Print the xy plane on z=0 for debugging."
        dd = defaultdict(list)
        for x, yz in self.pocket.items():
            for y in yz.keys():
                dd[y].append(x)
        for row, values in dd.items():
            print("".join([self._text(self.pocket[x][row][0]) for x in values]))

    @staticmethod
    def _text(value: bool) -> str:
        return "#" if value else "."

    def _y_values(self):
        return defaultdict(self._z_values)

    @staticmethod
    def _z_values():
        return defaultdict(bool)

    def _get_neighbours(self, x, y, z, state) -> List[bool]:
        neighbours = []
        for nx in [x - 1, x, x + 1]:
            for ny in [y - 1, y, y + 1]:
                for nz in [z - 1, z, z + 1]:
                    if (nx, ny, nz) == (x, y, z):
                        continue  # that's not a neighbour
                    neighbours.append(state[nx][ny][nz])
        return neighbours

    @staticmethod
    def _switch(cube: bool, prox: List[bool]):
        """Set cube state depending on all cubes in it's direct proximity"""
        if cube and prox.count(True) not in [2, 3]:
            return False
        if not cube and prox.count(True) == 3:
            return True
        return cube


pocket = Pocket(data, 3)
for _ in range(6):
    pocket.cycle()

print(
    f"""
    Puzzle number 1:
    Total active cubes is {pocket.active}
    """
)

# puzzle 2

print(
    f"""
    Puzzle number 2:
    
    """
)
