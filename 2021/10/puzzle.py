import math
import os
import sys
from typing import Dict, List, Optional

dir = os.path.dirname(__file__)
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_lines("input.txt", dir)

opener: List[str] = ["[", "{", "<", "("]
closer: Dict[str, str] = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">",
}
syntax_score: Dict[str, int] = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
autocompletion_scores: Dict[str, int] = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def check_syntax(line: str) -> Optional[str]:
    open_buffer: List[str] = []
    for char in line:
        if char in opener:
            open_buffer.append(char)
        elif char == closer[open_buffer[-1]]:
            # find the closer for the last added opener, compare with char
            del open_buffer[-1]
        else:
            return char


def calculate_syntax_score() -> int:
    score = 0
    for line in data:
        syntax_fault = check_syntax(line)
        if syntax_fault:
            score += syntax_score[syntax_fault]
    return score


def get_autocompletion(line: str) -> str:
    open_buffer: List[str] = []
    for char in line:
        if char in opener:
            open_buffer.append(char)
        elif char == closer[open_buffer[-1]]:
            # find the closer for the last added opener, compare with char
            del open_buffer[-1]
    # Line is done, now let's close the open_buffer
    autocompletion: List[str] = []
    for char in open_buffer[::-1]:
        autocompletion.append(closer[char])
    return "".join(autocompletion)


def autocomplete_score(completion: str) -> int:
    score = 0
    for char in completion:
        score = score * 5
        score += autocompletion_scores[char]
    return score


def get_middle_autocomplete_score() -> int:
    autocomplete_scores: List[int] = []
    lines = [line for line in data if not check_syntax(line)]
    for line in lines:
        autocomplete_scores.append(autocomplete_score(get_autocompletion(line)))
    autocomplete_scores.sort()
    return autocomplete_scores[math.floor(len(autocomplete_scores) / 2)]


# 1. find an discard corruped

# puzzle 1
print(
    f"""
    Puzzle number 1:
    
    The total score = {calculate_syntax_score()}
    """
)

# puzzle 2

print(
    f"""
    Puzzle number 2:
    
    Middle autocomplete score: {get_middle_autocomplete_score()}
    """
)
