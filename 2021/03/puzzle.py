import os
import sys
from collections import defaultdict
from copy import deepcopy

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files, utils  # noqa E402

diagnostics = files.read_lines("input.txt", dir)


def count_common(numbers):
    # count occurence of bits in a list of numbers
    # c[index] > 0 means "1" bit most common
    # c[index] < 0 means "0" bit most common
    # c[index] == 0 means both bits equally common
    c = defaultdict(int)
    for number in numbers:
        for index, bit in enumerate(number):
            c[index] = c[index] + 1 if bit == "1" else c[index] - 1
    return c


# puzzle 1
common = count_common(diagnostics)
gamma = "".join(["1" if x > 0 else "0" for x in common.values()])
epsilon = "".join(["1" if x < 0 else "0" for x in common.values()])

print(
    f"""
    Puzzle number 1:
    Power consumption is {int(gamma, base=2) * int(epsilon, base=2)}
    """
)


# puzzle 2
def oxy_match(count, bit):
    if count == 0 and bit == "1":
        return True
    if count < 0 and bit == "0":
        return True
    if count > 0 and bit == "1":
        return True
    return False


def co2_match(count, bit):
    if count == 0 and bit == "0":
        return True
    if count < 0 and bit == "1":
        return True
    if count > 0 and bit == "0":
        return True
    return False


oxy = deepcopy(diagnostics)
co2 = deepcopy(diagnostics)

for index in range(len(common)):
    count_oxy = count_common(oxy)[index]
    count_co2 = count_common(co2)[index]
    for number in diagnostics:
        if not oxy_match(count_oxy, number[index]) and number in oxy and len(oxy) > 1:
            # breakpoint()
            oxy.remove(number)
        if not co2_match(count_co2, number[index]) and number in co2 and len(co2) > 1:
            co2.remove(number)

print(
    f"""
    Puzzle number 2:
    Life support rating is {int(oxy[0], base=2) * int(co2[0], base=2)}
    """
)
