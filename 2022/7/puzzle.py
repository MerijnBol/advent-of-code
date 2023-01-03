import os
import sys
from collections import defaultdict
from typing import List, Tuple

dir = os.path.dirname(__file__)
# Use command flag to switch between test and real input.
testing: bool = len(sys.argv) > 1 and sys.argv[1] == "test"
input_filename: str = "test.txt" if testing else "input.txt"
sys.path.append(os.path.join(dir, "../.."))
from tools import files, utils  # noqa E402

data = files.read_lines(input_filename, dir)


class PuzzleSolution:
    def __init__(self, data) -> None:
        self._DATA = data
        self.load_data(data)
        print(f"Puzzle 1 result: {self.solution_1()}")
        print(f"Puzzle 2 result: {self.solution_2()}")

    def load_data(self, data):
        # Files are stored as a list of (name, size) tuples, with as key their path.
        self.workdir = "/"
        self.filesystem = {self.workdir: []}

        for line in data:
            if "$ cd" in line:
                # handle changing workdir
                self.change_dir(line)
            elif "$ ls" in line:
                # ignore
                ...
            else:
                self.log_output(line)

    def log_output(self, line: str):
        """Store files given by ``ls`` commands."""
        mode, name = line.split()
        if mode == "dir":
            # Add this dir (complete path) in storage.
            self.filesystem[self._new_workdir(name)] = []
        else:
            self.filesystem[self.workdir].append((name, int(mode)))

    def change_dir(self, command: str):
        if command == "$ cd /":
            self.workdir = "/"
        elif command == "$ cd ..":
            # remove deepest dir
            parts = self.workdir.split("/")
            parts.pop()  # ditch last dir
            self.workdir = "/".join(parts)
        else:
            dirname = command.split()[2]
            self.workdir = self._new_workdir(dirname)

    def _new_workdir(self, dirname: str) -> str:
        """Append dirname to current workdir"""
        if self.workdir == "/":
            return f"/{dirname}"
        else:
            return self.workdir + f"/{dirname}"

    def get_dir_size(self, target: str) -> int:
        dirs = set([target])
        for dir in self.filesystem.keys():
            if dir.startswith(target):
                dirs.add(dir)
        total = 0
        for dir in dirs:
            total += sum([file[1] for file in self.filesystem[dir]])
        return total

    def solution_1(self):
        small_dirs = []
        threshold = 100_000

        for dir in self.filesystem.keys():
            size = self.get_dir_size(dir)
            if size <= threshold:
                small_dirs.append(size)
        return sum(small_dirs)

    def solution_2(self):
        self.load_data(self._DATA)  # Reset state.
        MAX_USED = 40_000_000
        to_delete = self.get_dir_size("/") - MAX_USED

        possibilities: List[Tuple[str, int]] = []  # (path, size)
        for dir in self.filesystem.keys():
            size = self.get_dir_size(dir)
            if size >= to_delete:
                possibilities.append((dir, size))

        possibilities.sort(key=lambda a: a[1])
        return possibilities[0][1]


PuzzleSolution(data)
