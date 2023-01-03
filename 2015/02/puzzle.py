import os
import sys

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files  # noqa E402

dimensions = [
    tuple([int(val) for val in box.split("x")])
    for box in files.read_lines("input.txt", dir)
]


def paper_required(l: int, w: int, h: int) -> int:
    sizes = [l, w, h]
    sizes.sort()
    return 3 * sizes[0] * sizes[1] + 2 * sizes[1] * sizes[2] + 2 * sizes[2] * sizes[0]


def ribbon_required(l: int, w: int, h: int) -> int:
    sizes = [l, w, h]
    sizes.sort()
    return 2 * sizes[0] + 2 * sizes[1] + l * w * h


# puzzle 1
total_area = 0
for l, w, h in dimensions:
    total_area += paper_required(l, w, h)

print(
    f"""
    Puzzle number 1:
    Total area required is: {total_area}
    """
)

# puzzle 2
ribbon = 0
for l, w, h in dimensions:
    ribbon += ribbon_required(l, w, h)

print(
    f"""
    Puzzle number 2:
    Total ribbon required is: {ribbon}
    """
)
