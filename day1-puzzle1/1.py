import os

dirty_list = open("list.txt", "r").readlines()
numbers = []
for i in dirty_list:
    numbers.append(float( i.rstrip("/n") ))

def find_sum(numbers, total):
    for i in numbers:
        for j in numbers:
            if i + j == total:
                return i, j

total = 2020
num1, num2 = find_sum(numbers, total)

print(f"The first matching set of numbers, totalling {total} we found are {num1} and {num2}. This gives the total of:\n\n {int(num1 * num2)} ")