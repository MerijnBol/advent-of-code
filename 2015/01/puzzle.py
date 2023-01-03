import os
import sys

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files  # noqa E402

instructions = [char for char in files.read_lines("input.txt", dir)[0]]


def calculate_floor(floor: int, instruction: str) -> int:
    if instruction == "(":
        return floor + 1
    elif instruction == ")":
        return floor - 1
    return floor


# puzzle 1
floor = 0
for instruction in instructions:
    floor = calculate_floor(floor, instruction)

print(
    f"""
    Puzzle number 1:
    THe resulting floor is {floor}
    """
)

# puzzle 2
counter = 0
floor = 0
for instruction in instructions:
    floor = calculate_floor(floor, instruction)
    counter += 1
    if floor < 0:
        break

print(
    f"""
    Puzzle number 2:
    Reached basement on instruction {counter}
    """
)
