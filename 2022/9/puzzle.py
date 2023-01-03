import os
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
    def __init__(self, data) -> None:
        self._DATA = data
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        self.knots: List[Tuple[int, int]] = [(0, 0), (0, 0)]  # (X, Y)
        self.commands: List[Tuple(str, int)] = []
        for command in data:
            direction, distance = command.split(" ")
            self.commands.append((direction, int(distance)))

    def move_head(self, direction: str):
        """Move head 1 step in given direction."""
        hx, hy = self.knots[0]
        if direction == "U":
            hy = hy + 1
        elif direction == "D":
            hy = hy - 1
        elif direction == "R":
            hx = hx + 1
        elif direction == "L":
            hx = hx - 1
        else:
            raise Exception("Invalid direction")
        self.knots[0] = (hx, hy)

        for index in range(len(self.knots)):
            if index == 0:
                # skip the head
                continue
            self.knots[index] = self.move_knot(self.knots[index], self.knots[index - 1])

    @staticmethod
    def move_knot(knot: Tuple[int, int], predecessor: Tuple[int, int]):
        """Return new position of knot given location of it's predecessor."""
        delta_x = predecessor[0] - knot[0]
        delta_y = predecessor[1] - knot[1]
        tx, ty = knot
        if abs(delta_x) > 1:
            tx = tx + int(delta_x / abs(delta_x))
            if abs(delta_y) > 0:
                # Need to move diagonally
                ty = ty + int(delta_y / abs(delta_y))
        elif abs(delta_y) > 1:
            ty = ty + int(delta_y / abs(delta_y))
            if abs(delta_x) > 0:
                # Need to move diagonally
                tx = tx + int(delta_x / abs(delta_x))
        return (tx, ty)

    def solution_1(self):
        unique_tail_pos = set([self.knots[1]])
        for dir, dist in self.commands:
            for _ in range(dist):
                # Move 'dist' amount of times in 'dir' direction.
                self.move_head(dir)
                unique_tail_pos.add(self.knots[1])
        return len(unique_tail_pos)

    def solution_2(self):
        self.load_data(self._DATA)  # Reset state.
        self.knots = [(0, 0)] * 10  # Make it 10 ropes
        unique_tail_pos = set([self.knots[-1]])
        for dir, dist in self.commands:
            for _ in range(dist):
                # Move 'dist' amount of times in 'dir' direction.
                self.move_head(dir)
                unique_tail_pos.add(self.knots[-1])
        return len(unique_tail_pos)


PuzzleSolution(data)
