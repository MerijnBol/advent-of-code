import os
import sys
from functools import cache
from typing import List

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

initial = [int(x) for x in files.read_lines("input.txt", dir)[0].split(",")]


def fuel(crabs: List[int], position: int):
    fuel = 0
    for crab in crabs:
        fuel += max(crab, position) - min(crab, position)
    return fuel


@cache
def calc_quad_fuel(delta: int) -> int:
    fuel = 0
    add = 0
    for _ in range(1, delta + 1):
        add += 1
        fuel += add
    return fuel


def fuel_quad(crabs: List[int], position: int):
    fuel = 0
    for crab in crabs:
        fuel += calc_quad_fuel(max(crab, position) - min(crab, position))
    return fuel


# puzzle 1
start = min(initial)
end = max(initial)
lowest = (end, fuel(initial, end))  # lowest = (position, fuel).
for pos in range(start, end):
    fuel_cost = fuel(initial, pos)
    if fuel_cost < lowest[1]:
        lowest = (pos, fuel_cost)


print(
    f"""
    Puzzle number 1:
    Position {lowest[0]} is cheapest to get to with a fuel cost of {lowest[1]}
    """
)

# puzzle 2
start = min(initial)
end = max(initial)
lowest = (end, fuel_quad(initial, end))  # lowest = (position, fuel).
for pos in range(start, end):
    fuel_cost = fuel_quad(initial, pos)
    if fuel_cost < lowest[1]:
        lowest = (pos, fuel_cost)

print(
    f"""
    Puzzle number 2:
    Position {lowest[0]} is cheapest to get to with a fuel cost of {lowest[1]}
    """
)
