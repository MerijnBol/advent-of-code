import os
import re
import sys
from collections import defaultdict
from typing import Dict, List, Tuple

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_file(input_filename, dir)


class PuzzleSolution:
    def __init__(self, data) -> None:
        self._data = data
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        raw_state, raw_commands = data.split("\n\n")
        raw_state = raw_state.split("\n")
        numbers_row = raw_state.pop()

        self.towers: Dict[int, List[str]] = defaultdict(list)
        for line in raw_state[::-1]:
            for count, index in enumerate(range(1, len(numbers_row), 4), start=1):
                if crate := line[index].strip():
                    self.towers[count].append(crate)

        self.commands: List[Tuple[int, int, int]] = []
        for line in raw_commands.rstrip().split("\n"):
            numbers = [int(x) for x in re.findall("\d{1,}", line)]
            if not len(numbers) == 3:
                breakpoint()
            self.commands.append(tuple(numbers))

    def handle_commands(
        self, command: Tuple[int, int, int], multistack_crane: bool = False
    ):
        count, source, dest = command
        stack = self.towers[source][-count:]
        if not multistack_crane:
            stack.reverse()  # Because they're moved 1 by 1
        del self.towers[source][-count:]
        self.towers[dest] += stack

    def solution_1(self):
        for command in self.commands:
            self.handle_commands(command)
        return "".join([tower[-1] for tower in self.towers.values()])

    def solution_2(self):
        # reset state
        self.load_data(self._data)
        for command in self.commands:
            self.handle_commands(command, multistack_crane=True)
        return "".join([tower[-1] for tower in self.towers.values()])


PuzzleSolution(data)
