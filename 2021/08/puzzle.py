import os
import sys
from typing import Dict, List, Tuple

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

entries = [
    tuple(([x for x in combis.split()] for combis in entry.split("|")))
    for entry in files.read_lines("input.txt", dir)
]

connection = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
unique_lengths = {
    # number of bars : int value
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}


# puzzle 1
unique_numbers = 0
for _, output in entries:
    for num in output:
        if len(num) in unique_lengths:
            unique_numbers += 1

print(
    f"""
    Puzzle number 1:
    The output of all entries contain {unique_numbers} unique numbers.
    """
)

# puzzle 2


def get_total(combi: Tuple[List[str], List[str]]) -> int:
    actual = {}
    unmatched_5 = []  # values 2, 3, 5
    unmatched_6 = []  # values 0, 6, 9
    # Find the identifiable combinations, sort the ambiguous ones.
    for num in combi[1]:
        if len(num) in unique_lengths:
            actual[num] = unique_lengths[len(num)]
        elif len(num) == 5:
            unmatched_5.append(num)
        else:
            unmatched_6.append(num)
    assert all([len(x) == 6 for x in unmatched_6])

    # Get the bars that form the number 1
    for x in combi[0]:
        if len(x) == 2:
            one_combination = x
            break
    assert one_combination

    # count how many times a wire is used for the 10 numbers
    all_chars = "".join(combi[0])
    counts = {}
    for char in "abcdefg":
        counts[all_chars.count(char)] = char

    # Differentiate 0, 6 and 9.
    for num in unmatched_6:
        if not all(x in num for x in one_combination):
            # 0 and 9 will have all bars of 1 in them.
            actual[num] = 6
        elif counts[4] in num:
            # the bar that will be used 4 times to get all 10 numbers, is only
            # used for 0, not for 9.
            actual[num] = 0
        else:
            actual[num] = 9

    # Differentiate 2, 3 and 5
    for num in unmatched_5:
        if all(x in num for x in one_combination):
            # Only 3 contains wiring from a 1
            actual[num] = 3
        elif counts[9] in num:
            # The wire that will be needed 9 times to get all numbers, is only
            # used for 2, not 5
            actual[num] = 5
        else:
            # only 5 left
            actual[num] = 2
    # print(int("".join([str(actual[text]) for text in combi[1]])))
    return int("".join([str(actual[text]) for text in combi[1]]))


total = 0
for entry in entries:
    total += get_total(entry)

print(
    f"""
    Puzzle number 2:
    The total value is {total}
    """
)
