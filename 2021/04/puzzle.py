import os
import sys
from copy import deepcopy
from typing import Dict, List, Optional, Tuple

import numpy as np

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

lines = files.read_lines("input.txt", dir)
draw = [int(x) for x in lines[0].split(",")]
inputs = np.split(lines[1:], range(0, len(lines[1:]), 5))


class Board:
    grid: List[List[int]]
    mark: List[List[bool]]

    def __init__(self, input: List[str]):
        self.grid = []
        for row in input:
            self.grid.append([int(x) for x in row.split()])
        assert len(self.grid[0]) == 5
        assert len(self.grid) == 5
        self.mark = [[False for _ in range(5)] for _ in range(5)]
        assert len(self.mark[0]) == 5
        assert len(self.mark) == 5

    def mark_number(self, number):
        for row, content in enumerate(self.grid):
            for column, value in enumerate(content):
                if value == number:
                    self.mark[row][column] = True

    @property
    def full(self):
        # check rows
        for row in self.mark:
            if all([x for x in row]):
                return True
        # check columns
        for index in range(5):
            if all(row[index] for row in self.mark):
                return True
        # no win
        return False

    @property
    def unmarked_value(self) -> int:
        unmarked = 0
        for row, content in enumerate(self.mark):
            for column, value in enumerate(content):
                if not value:
                    unmarked += self.grid[row][column]
        return unmarked


boards = [Board(input) for input in inputs if len(input) > 0]


# puzzle 1
def find_first_board(numbers) -> Tuple[Optional[Board], int]:
    for num in numbers:
        for board in boards:
            board.mark_number(num)
            if board.full:
                return (board, num)
    return (None, numbers[-1])


winner, call = find_first_board(draw)
assert winner


print(
    """
    Puzzle number 1:
    The total computed score for the first winning card"""
    f"is {winner.unmarked_value * call}"
)


# puzzle 2
def find_last_board(numbers) -> Tuple[Optional[Board], int]:
    pruned = {x: deepcopy(y) for x, y in enumerate(boards)}
    keys = [x for x in pruned.keys()]
    for num in numbers:
        for key in keys:
            if key not in pruned:
                # Deleted
                continue
            pruned[key].mark_number(num)
            if pruned[key].full and len(pruned) == 1:
                return (pruned[key], num)
            if pruned[key].full and len(pruned) > 1:
                del pruned[key]
    return None, 0


last, call = find_last_board(draw)
assert last

print(
    f"""
    Puzzle number 2:
    The total computed score for the last winning card"""
    f"is {last.unmarked_value * call}"
)
