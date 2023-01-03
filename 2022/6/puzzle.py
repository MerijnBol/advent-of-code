import os
import sys

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_file(input_filename, dir)


class PuzzleSolution:
    def __init__(self, data) -> None:
        self._DATA = data
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        self.datastream: str = data

    def unique_char_marker(self, n: int = 4) -> int:
        """
        Return index of end of a marker of ``n`` length.
        """
        for index in range(0, len(self.datastream) - n):
            marker = self.datastream[index : index + n]
            if len(marker) == len(set(marker)):
                return index + n
        raise Exception("No marker found")

    def solution_1(self):
        return self.unique_char_marker()

    def solution_2(self):
        return self.unique_char_marker(n=14)


PuzzleSolution(data)
