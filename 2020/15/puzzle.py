import os
import sys
from typing import Dict, List, Tuple

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files  # noqa E402


class MemoryGame:
    counter: int
    last_spoken: int
    log: Dict[int, Tuple[int, int]]  # Tuple[age, last count]

    def __init__(self):
        self.counter = 1
        self.log = {}

    def handle_start(self, numbers: List[int]):
        for num in numbers:
            self._save_number(num)
            self.last_spoken = num
            self.counter += 1

    def run_turns(self, turns: int) -> int:
        part = turns / 20
        parts = 1
        while self.counter <= turns:
            new_number = self.log[self.last_spoken][0]
            self._save_number(new_number)
            self.last_spoken = new_number
            self.counter += 1
            if self.counter == part * parts:
                print(parts * ".", end="\r")
                parts += 1
        return self.last_spoken

    def _save_number(self, number):
        if number not in self.log:
            self.log[number] = (0, self.counter)
        self.log[number] = (self.counter - self.log[number][1], self.counter)


# puzzle 1
numbers = [int(num) for num in files.read_lines("input.txt", dir)[0].split(",")]
game = MemoryGame()
game.handle_start(numbers)


print(
    f"""
    Puzzle number 1:
    The 2020th number spoken is {game.run_turns(2020)}
    """
)

# puzzle 2

print(
    f"""
    Puzzle number 2:
    The 30 millionth unique number is: {game.run_turns(30_000_000)}
    """
)
