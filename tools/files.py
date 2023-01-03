from os import path
from typing import List


def read_lines(filename: str, dir: str) -> List[str]:
    """Return all non-empty lines."""
    with open(path.join(dir, filename), "r") as file:
        # Split lines, only return truthy values
        return [line for line in file.read().split("\n") if line]


def read_lines_preserve(filename: str, dir: str) -> List[str]:
    """Return all lines including empty lines."""
    with open(path.join(dir, filename), "r") as file:
        # Split lines, only return truthy values
        return [line for line in file.read().split("\n")]


def read_file(filename: str, dir: str) -> str:
    """Return file content."""
    with open(path.join(dir, filename), "r") as file:
        return file.read()
