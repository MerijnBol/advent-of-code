import itertools
import os
import string
import sys
from typing import List

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_lines(input_filename, dir)

PRIORITY = {char: prio for prio, char in enumerate(string.ascii_letters, start=1)}


class Rucksacks:
    _sacks: List[str]

    def __init__(self, data) -> None:
        self._sacks = list(data)

    @staticmethod
    def find_duplicate(content: str):
        half = int(len(content) / 2)
        comp1 = content[:half]
        comp2 = content[half:]
        for char in comp1:
            if char in comp2:
                return char
        raise Exception("No duplicate found")

    @staticmethod
    def get_group_char(group: List[str]) -> str:
        assert len(group) == 3
        g1, g2, g3 = group
        for char in g1:
            if char in g2 and char in g3:
                return char
        raise Exception("No badge found.")

    @property
    def get_priority_sum_duplicates(self) -> int:
        total = 0
        for content in self._sacks:
            total += PRIORITY[self.find_duplicate(content)]
        return total

    @property
    def get_group_badge_prio_sum(self) -> int:
        total = 0
        for index in range(0, len(self._sacks), 3):
            # SPlit into groups of three
            char = self.get_group_char(self._sacks[index : index + 3])
            total += PRIORITY[char]
        return total


rs = Rucksacks(data)
# puzzle 1

print(
    f"""
    Puzzle number 1:
    
    Sum of priorities is {rs.get_priority_sum_duplicates}
    """
)

# puzzle 2

print(
    f"""
    Puzzle number 2:

    Sum of priorities is {rs.get_group_badge_prio_sum}
    """
)
