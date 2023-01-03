import os
import sys
from functools import reduce

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

measurements = [int(x) for x in files.read_lines("input.txt", dir)]


# puzzle 1
increase = 0
for index, measurement in enumerate(measurements, start=1):
    if index < len(measurements) and measurements[index] > measurement:
        increase += 1

print(
    f"""
    Puzzle number 1:
    Measurements increased {increase} times.
    """
)

# puzzle 2
increase_window = 0
for index, _ in enumerate(measurements[3:], start=3):
    if sum(measurements[index - 3 : index]) < sum(measurements[index - 2 : index + 1]):
        increase_window += 1

print(
    f"""
    Puzzle number 2:
    Measurement window increased {increase_window} times.
    """
)
