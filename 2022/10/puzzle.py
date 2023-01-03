import os
import sys
from typing import List, Tuple

import numpy as np

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_lines(input_filename, dir)


class PuzzleSolution:
    def __init__(self, data) -> None:
        self._DATA = data
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        self.command_list: List[Tuple[str, int]] = []
        for raw in data:
            parts = raw.split(" ")
            command = parts[0]
            if command == "addx":
                value = int(parts[1])
            else:
                value = 0
            self.command_list.append((command, value))
        self.commands = iter(self.command_list)
        self.cycle = 0
        self.x_register = 1
        self.signal_strength = 0
        self.crt_rows = []

    def run_program(self):
        """
        Run the computer.

        Each loop of the 'While True' loop is a cycle. New commands are
        fetched on demand from the self.commands Iterator.
        """
        in_progress_timer = 0
        command: Tuple[str, int] = ("", 0)
        try:
            while True:
                if in_progress_timer > 0:
                    in_progress_timer -= 1
                else:
                    if command[0] == "addx":
                        # Finalise in-memory command.
                        self.x_register += command[1]
                    # Get new command from list.
                    command = next(self.commands)
                    if command[0] == "addx":
                        # Add the 'addx' command to memory
                        in_progress_timer = 1

                # increment cycle counter
                self.cycle += 1

                self.draw_crt()

                # Store signal strength
                if self.cycle in [20, 60, 100, 140, 180, 220]:
                    self.signal_strength += self.cycle * self.x_register

        except StopIteration:
            # No more commands left
            pass

    def draw_crt(self):
        """
        Draw pixels on the screen.

        The 2d map is represented in a 1d array. Since x_register only
        works in 2D (so max lenght of 20 pixels), the cycle number is
        amended to also work with max 40 width.
        """
        sprite_indexes = range(self.x_register, self.x_register + 3)
        one_dim_cycle = self.cycle % 40
        if one_dim_cycle in sprite_indexes:
            self.crt_rows.append("#")
        else:
            self.crt_rows.append(".")

    def solution_1(self):
        self.run_program()
        return self.signal_strength

    def solution_2(self):
        self.load_data(self._DATA)  # Reset state.
        self.run_program()

        printlist = np.array_split(self.crt_rows, 6)
        for row in printlist:
            print("".join(row))


PuzzleSolution(data)
