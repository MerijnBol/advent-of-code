import os
import sys
from copy import deepcopy
from functools import reduce
from itertools import chain
from pprint import pprint
from typing import Dict, List

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

# Unpack all data
data = files.read_lines("input.txt", dir)
cut1 = data.index("your ticket:")
cut2 = data.index("nearby tickets:")
rules_raw = data[:cut1]
ticket = [int(x) for x in data[cut1 + 1 : cut2][0].split(",")]
nearby = [[int(y) for y in x.split(",")] for x in data[cut2 + 1 :]]

# Unpack rules
rules = {}
for rule in rules_raw:
    text, nums = rule.split(": ")
    rules[text] = [
        tuple([int(n) for n in numset.split("-")]) for numset in nums.split(" or ")
    ]


def in_range(number: int) -> bool:
    for ranges in rules.values():
        for range in ranges:
            if range[0] <= number <= range[1]:
                return True
    return False


# puzzle 1
flat_nearby = list(chain(*nearby))
print(
    f"""
    Puzzle number 1:
    Ticket scanning error rate is {sum([x for x in flat_nearby if not in_range(x)])}
    """
)

# puzzle 2
prune_nearby = deepcopy(nearby)
for tick in nearby:
    for number in tick:
        # Check if all numbers have at least one valid range.
        if not in_range(number):
            # Make sure we remove all occurences of 'tick'
            while tick in prune_nearby:
                prune_nearby.remove(tick)

# Helper to check one number agains all ranges in the rules
def valid_for_range(value, ranges):
    for range in ranges:
        if range[0] <= value <= range[1]:
            return True


def solve_text(_ticket: List, _rules: Dict, _translated={}):
    """
    Assign all words to the ticket.

    It's important to assume each word can only match one number on the ticket, because
    for at least one word this is probably true.
    """
    for index, number in enumerate(_ticket):
        temp_store = []
        for name, ranges in _rules.items():
            if (
                all([valid_for_range(x[index], ranges) for x in prune_nearby])
                and name not in _translated.values()
            ):
                temp_store.append((name))
        if len(temp_store) == 1:
            _translated[number] = temp_store[0]

    if not len(ticket) == len(_translated):
        # recurse to fill in the skipped words.
        solve_text(_ticket, _rules, _translated)

    return _translated


translated = solve_text(ticket, rules)


departure_fields = []
for key, value in translated.items():
    if value.count("departure"):
        departure_fields.append(key)

print(
    f"""
    Puzzle number 2:
    Multiplied values gives: {reduce((lambda x, y: x * y), departure_fields)}
    """
)
