import os
import sys
from typing import List, Tuple

dir = os.path.dirname(__file__)
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402


class ElveCalories:
    calories: List[int]

    def __init__(self, lines: str):
        self.calories = self.parse_input(lines)

    def parse_input(self, file_data: str) -> List[int]:
        calorie_totals = []

        for elve in file_data.split("\n\n"):
            calorie_totals.append(
                sum([int(food_cal) for food_cal in elve.split("\n") if food_cal])
            )

        return calorie_totals

    @property
    def maximum_cal_total(self) -> int:
        return max(self.calories)

    @property
    def sum_top_three(self) -> int:
        cal_copy = list(self.calories)
        cal_copy.sort(reverse=True)
        return sum(cal_copy[:3])


calories = ElveCalories(files.read_file(input_filename, dir))

# puzzle 1

print(
    f"""
    Puzzle number 1:
    
    The maximum calory total is: {calories.maximum_cal_total}
    """
)

# puzzle 2

print(
    f"""
    Puzzle number 2:
    
    Total calories of top 3 elves is: {calories.sum_top_three}
    """
)
