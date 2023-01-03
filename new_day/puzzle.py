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
        print("TODO: Parse and store testdata.")

    def solution_1(self):
        return "TODO: solve it"

    def solution_2(self):
        self.load_data(self._DATA)  # Reset state.
        return "TODO: Solve it"


PuzzleSolution(data)
