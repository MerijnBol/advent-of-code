import os
import sys
from typing import List, Optional, Tuple

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

games = files.read_lines(input_filename, dir)

# FIXME: this was a terrible design. Great for a refactor practice.


class BaseRPS:
    type: str
    score: int

    def do_i_win(self, opponent: "BaseRPS") -> Optional[bool]:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Rock(BaseRPS):
    type = "ROCK"
    score = 1

    def do_i_win(self, opponent: BaseRPS) -> Optional[bool]:
        if opponent.type == "SCISSORS":
            return True
        if opponent.type == "PAPER":
            return False
        if opponent.type == self.type:
            return None
        raise ValueError("Did not get a rock paper or scissor.")


class Paper(BaseRPS):
    type = "PAPER"
    score = 2

    def do_i_win(self, opponent: BaseRPS) -> Optional[bool]:
        if opponent.type == "ROCK":
            return True
        if opponent.type == "SCISSORS":
            return False
        if opponent.type == self.type:
            return None
        raise ValueError("Did not get a rock paper or scissor.")


class Scissors(BaseRPS):
    type = "SCISSORS"
    score = 3

    def do_i_win(self, opponent: BaseRPS) -> Optional[bool]:
        if opponent.type == "PAPER":
            return True
        if opponent.type == "ROCK":
            return False
        if opponent.type == self.type:
            return None
        raise ValueError("Did not get a rock paper or scissor.")


MOVE_MAP = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors(),
}


def winscore(result: Optional[bool]) -> int:
    if result is not None:
        return 6 if result else 0
    else:
        return 3


class RPSChecker:
    # Opponent move, my move, did I win?
    results: List[Tuple[BaseRPS, BaseRPS, Optional[bool]]]

    def __init__(self, games: List[str], plan_b=False) -> None:
        self.results = []
        if plan_b:
            # Second column defines if i should win or lose
            for game in games:
                opp, command = game.split()
                opp = MOVE_MAP[opp]
                if command == "Y":
                    # Draw
                    me = opp
                elif command == "Z":
                    # win
                    me = self.find_required_result(opp, True)
                elif command == "X":
                    # lose
                    me = self.find_required_result(opp, False)
                else:
                    raise Exception("no command")
                self.results.append((opp, me, me.do_i_win(opp)))
        else:
            for game in games:
                opp, me = game.split()
                opp = MOVE_MAP[opp]
                me = MOVE_MAP[me]
                self.results.append((opp, me, me.do_i_win(opp)))

    @property
    def total_score(self) -> int:
        score = 0
        for result in self.results:
            _, me, result = result
            score += me.score + winscore(result)
        return score

    @staticmethod
    def find_required_result(opponent: BaseRPS, result: bool) -> BaseRPS:
        types = [Rock(), Paper(), Scissors()]
        for type in types:
            if type.do_i_win(opponent) == result:
                return type
        raise Exception("Couldn't find result")


checker = RPSChecker(games)

# puzzle 1

print(
    f"""
    Puzzle number 1:
    
    Total score = {checker.total_score}
    """
)

# puzzle 2

print(
    f"""
    Puzzle number 2:
    
    Total score = {RPSChecker(games, plan_b=True).total_score}
    """
)
