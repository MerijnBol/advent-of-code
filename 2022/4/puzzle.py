import os
import re
import sys
from typing import List, Tuple

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_lines(input_filename, dir)


class PuzzleSolution:
    pairs: List[Tuple[int, int, int, int]]

    def __init__(self, data) -> None:
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        self.pairs = []
        for rawpair in data:
            p1a, p1b, p2a, p2b = re.split("-|,", rawpair)
            self.pairs.append((int(p1a), int(p1b), int(p2a), int(p2b)))

    @staticmethod
    def has_full_overlap(pair: Tuple[int, int, int, int]) -> bool:
        elf_1_start, elf_1_end, elf_2_start, elf_2_end = pair

        if elf_1_start <= elf_2_start and elf_1_end >= elf_2_end:
            return True

        if elf_1_start >= elf_2_start and elf_1_end <= elf_2_end:
            return True

        return False

    @staticmethod
    def has_some_overlap(pair: Tuple[int, int, int, int]) -> bool:
        range_1 = [x for x in range(pair[0], pair[1] + 1)]
        range_2 = [x for x in range(pair[2], pair[3] + 1)]

        for x in range_1:
            if x in range_2:
                return True
        return False

    def solution_1(self):
        full_overlap = 0
        for pair in self.pairs:
            if self.has_full_overlap(pair):
                full_overlap += 1
        return full_overlap

    def solution_2(self):
        overlap = 0
        for pair in self.pairs:
            if self.has_some_overlap(pair):
                overlap += 1
        return overlap


PuzzleSolution(data)
