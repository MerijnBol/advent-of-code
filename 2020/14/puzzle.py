import os
import re
import sys
from copy import deepcopy
from typing import Dict, List, Union

dir = os.path.dirname(__file__)
sys.path.append("/home/merijn/software/advent-of-code")
from pprint import pprint

from tools import files  # noqa E402


class Memory:
    mask: str
    bitsize: int
    bitloop: List[int]
    store: Dict[int, str]

    def __init__(self, bitsize=36):
        self.bitsize = bitsize
        self.bitloop = [x for x in range(36)]
        self.mask = ""
        self.store = {}

    def set_mask(self, mask: str):
        assert len(mask) == 36
        self.mask = mask

    def apply_instruction(self, pointer: str, value: str):
        pointer_val = re.search(r"\d+", pointer)
        assert pointer_val

        decimal = self._base10_to_decimal(value)
        upfill = 36 - len(decimal)
        bit = upfill * "0" + decimal

        newbit = ""
        for index in self.bitloop:
            newbit = (
                newbit + self.mask[index]
                if self.mask[index] in ["0", "1"]
                else newbit + bit[index]
            )

        self.store[int(pointer_val.group())] = newbit

    def emulate_mad(self, raw_pointer: str, value: str):
        pointer_val = re.search(r"\d+", raw_pointer)
        assert pointer_val
        pointer_dec = self._base10_to_decimal(pointer_val.group())
        upfill = 36 - len(pointer_dec)
        pointer = upfill * "0" + pointer_dec

        # Apply mask to pointer
        newpointer = ""
        for index in self.bitloop:
            newpointer = (
                newpointer + self.mask[index]
                if self.mask[index] in ["X", "1"]
                else newpointer + pointer[index]
            )

        # write value to all pointers
        dec_value = self._base10_to_decimal(value)
        all_pointers = self._float_bits([newpointer])
        for pointer in all_pointers:
            key = self._decimal_to_base10(pointer)
            self.store[key] = dec_value

    def _base10_to_decimal(self, base10: str) -> str:
        return "{0:b}".format(int(base10))

    def _decimal_to_base10(self, decimal: str) -> int:
        return int(decimal, base=2)

    def _float_bits(self, slots: List[str]) -> List[str]:
        for bit in slots:
            if bit.count("X") > 0:
                slots.remove(bit)
                slots.append(bit.replace("X", "0", 1))
                slots.append(bit.replace("X", "1", 1))
                self._float_bits(slots)
        return slots

    @property
    def bitsum(self) -> int:
        sum = 0
        for decimal in self.store.values():
            sum += self._decimal_to_base10(decimal)

        return sum


# puzzle 1
memory = Memory()

instructions = [x.split(" = ") for x in files.read_lines("input.txt", dir)]
for key, value in instructions:
    mask = ""
    mem_init: List[List[str]] = []

    if key == "mask":
        memory.set_mask(value)
    elif key[:3] == "mem":
        memory.apply_instruction(key, value)


print(
    f"""
    Puzzle number 1:
    Sum of all converted bits is: {memory.bitsum}
    """
)

# puzzle 2

mem2 = Memory()

instructions = [x.split(" = ") for x in files.read_lines("input.txt", dir)]
for key, value in instructions:
    if key == "mask":
        mem2.set_mask(value)
        assert mem2.mask == value
    elif key[:3] == "mem":
        mem2.emulate_mad(key, value)


print(
    f"""
    Puzzle number 2:
    Sum of all converted bits is: {mem2.bitsum}
    """
)
