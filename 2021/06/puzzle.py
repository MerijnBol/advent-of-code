import os
import sys
from copy import deepcopy
from typing import List

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

initial_state = [int(x) for x in files.read_lines("input.txt", dir)[0].split(",")]


def sim_for_days(fish: List[int], total_days: int) -> int:
    """
    Simulate fish increase for given amount of days.
    """
    store = {}
    for i in range(9):
        store[i] = 0

    # Fill the store with the current fish counts
    for f in fish:
        store[f] += 1

    days = 0
    while days < total_days:
        temp = {}
        for key in store.keys():
            if key == 8:
                temp[key] = store[0]
                continue
            if key == 6:
                temp[key] = store[0] + store[7]
                continue
            # besides 6 and 8, just fill with fish from day before.
            temp[key] = store[key + 1]
        days += 1
        store = temp

    return sum(store.values())


# puzzle 1
fish = sim_for_days(initial_state, 80)

print(
    f"""
    Puzzle number 1:
    Total fish after 80 days is {fish}
    """
)

# puzzle 2

fish = sim_for_days(initial_state, 256)

print(
    f"""
    Puzzle number 2:
    Total fish after 256 days is {fish}
    """
)
