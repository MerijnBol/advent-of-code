import os
import sys
from hashlib import md5

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files  # noqa E402


def hash_starting_with_zeros(count: int) -> int:
    prefix = "bgvyzdsv"
    postfix = 1
    while True:
        hash = md5(bytes(prefix + str(postfix), "utf8")).hexdigest()
        if all([char == "0" for char in hash[:count]]):
            break
        postfix += 1

    return postfix


# puzzle 1
print(
    f"""
    Puzzle number 1:
    Smallest number giving desired hash is {hash_starting_with_zeros(5)}
    """
)

# puzzle 2
print(
    f"""
    Puzzle number 2:
    Smallest number giving desired hash is {hash_starting_with_zeros(6)}
    """
)
