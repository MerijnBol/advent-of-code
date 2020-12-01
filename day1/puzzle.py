import os

def get_list():
    dirty_list = open("list.txt", "r").readlines()
    numbers = []
    for i in dirty_list:
        numbers.append(float( i.rstrip("/n") ))
    return numbers

def find_sum_of_two(numbers, total):
    for i in numbers:
        for j in numbers:
            if i + j == total:
                return i, j

def find_sum_of_three(numbers, total):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == total:
                    return i, j, k

def answer_puzzle_1():
    total = 2020
    num1, num2 = find_sum_of_two(get_list(), total)
    print(f"The first matching set of numbers, totalling {total} we found are {num1} and {num2}. This gives the total of:\n\n {int(num1 * num2)} ")

def answer_puzzle_2():
    total = 2020
    num1, num2, num3 = find_sum_of_three(get_list(), total)
    print(f"The first matching set of numbers, totalling {total} we found are {num1}, {num2} and {num3}. This gives the total of:\n\n {int(num1 * num2 * num3)} ")

answer_puzzle_2()