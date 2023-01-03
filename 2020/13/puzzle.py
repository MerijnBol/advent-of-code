import os
import sys
from functools import cache
from typing import Generator, List, Tuple, Union

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from tools import files  # noqa E402

departure = int(files.read_lines("input.txt", dir)[0])
busses = []
for bus in files.read_lines("input.txt", dir)[1].split(","):
    try:
        busses.append(int(bus))
    except ValueError:
        continue


def bus_wait_time(time: int, bus_id: int) -> int:
    remainder = time % bus_id
    return 0 if remainder == 0 else bus_id - remainder


# puzzle 1
wait_time = {}
for bus in busses:
    wait_time[bus] = bus_wait_time(departure, bus)

shortest_wait = min(zip(wait_time.values(), wait_time.keys()))

print(
    f"""
    Puzzle number 1:
    Shortest wait * bus's ID = {shortest_wait[0] * shortest_wait[1]}
    """
)

# puzzle 2

bus_indexed: List[Tuple[int, int]] = []  # (offset, bus_id)
for offset, bus in enumerate(files.read_lines("input.txt", dir)[1].split(",")):
    try:
        bus_id = int(bus)
    except ValueError:
        continue
    bus_indexed.append((bus_id, offset))

bus_indexed.sort()


def valid_offset(time: int, bus: Tuple[int, int]) -> bool:
    """Determine if a departure time will fulfill the offset requirements."""
    bus_id, offset = bus

    required_bus_departure = time + offset

    return required_bus_departure % bus_id == 0


def valid_matches(time, gap, busses) -> tuple[int, int]:
    """
    When starting on a certain time, check if all busses fulfill the requirements.

    If they do, log the time. This time will be used to start from in the new loop.
    Also log a second value where all busses are valid. The gap between these values
    is the new step_value (or gap).
    """
    values = []
    while len(values) < 2:
        if all(valid_offset(time, bus) for bus in busses):
            values.append(time)
        time += gap
    return (values[0], values[1] - values[0])


print(f"We have to calculate for {len(bus_indexed)} busses. Let's go.")
departure = 1
step_size = 1
busses_being_checked = []
for index, bus in enumerate(bus_indexed):
    # Add a new bus to the list in each loop. to gradually increase the calculation
    # difficulty. Not doing this will mean the step sizes are way too small, causing the
    # calculation to never finish.
    busses_being_checked.append(bus)
    print(
        f"Starting check for bus {len(busses_being_checked)}. Current step size is {step_size}."
    )
    departure, step_size = valid_matches(departure, step_size, busses_being_checked)

print(
    f"""
    Puzzle number 2:
    First departure fulfilling requirements is: {departure}
    """
)
