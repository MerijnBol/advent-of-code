import os
import sys
from collections import defaultdict
from typing import Tuple

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files  # noqa E402

instructions = [char for char in files.read_lines("input.txt", dir)[0]]


def move(instruction: str, coor: Tuple[int, int]) -> tuple[int, int]:
    x, y = coor
    if instruction == ">":
        x += 1
    if instruction == "<":
        x -= 1
    if instruction == "^":
        y += 1
    if instruction == "v":
        y -= 1
    return (x, y)


# puzzle 1
addresses = defaultdict(int)
location = (0, 0)
addresses[str(location)] += 1

for instruction in instructions:
    location = move(instruction, location)
    addresses[str(location)] += 1

print(
    f"""
    Puzzle number 1:
    Total houses visited: {len(addresses)}
    """
)


# puzzle 2
addresses = defaultdict(int)
loc_santa = (0, 0)
loc_robo = (0, 0)
addresses[str((0, 0))] = 2


def split_work() -> Tuple[str, str]:
    gen = (str(instr) for instr in instructions)
    for inst in gen:
        yield (inst, next(gen))


for santa, robo in split_work():
    loc_santa = move(santa, loc_santa)
    addresses[str(loc_santa)] += 1
    loc_robo = move(robo, loc_robo)
    addresses[str(loc_robo)] += 1


print(
    f"""
    Puzzle number 2:
    Total houses visited: {len(addresses)}
    """
)
