import os
import sys

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

commands = [
    (cmnd.split()[0], int(cmnd.split()[1]))
    for cmnd in files.read_lines("input.txt", dir)
]

# puzzle 1
forward = 0
depth = 0
for command, value in commands:
    if command == "forward":
        forward += value
    if command == "up":
        depth -= value
    if command == "down":
        depth += value

print(
    f"""
    Puzzle number 1:
    Product of end values is {forward * depth}
    """
)

# puzzle 2
forward = 0
depth = 0
aim = 0
for command, value in commands:
    if command == "forward":
        forward += value
        depth += aim * value
    if command == "up":
        aim -= value
    if command == "down":
        aim += value
print(
    f"""
    Puzzle number 2:
    Product of end values is {forward * depth}
    """
)
