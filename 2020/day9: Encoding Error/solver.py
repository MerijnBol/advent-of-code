
def input():
    return [int(x.strip("\n")) for x in open("input.txt", "r").readlines()]

def check_xmas(puzzle, preamble):
    numbers = input()

    def make_pairs(index, preamble, numbers):
        row = numbers[(index - preamble):index].copy()
        result = []
        for i in row:
            for j in row:
                result.append(i + j)
        return result


    def loop_through_numbers(preamble):
        index = preamble

        # do the loop
        while index < len(numbers):
            ref = make_pairs(index, preamble, numbers)
            if numbers[index] not in ref:
                return False, numbers[index]
            index += 1
        return True, 0
    
    # puzzle 2 from here

    def check_for_index(index, target):
        total = 0
        new_index = index
        while total <= target:
            if total == target:
                return True, index, new_index
            total += numbers[new_index]
            new_index += 1
        return False, 0, 0
    
    def get_sum_of_minmax(i1, i2):
        values = numbers[i1:i2].copy()
        return (min(values) + max(values))

    def find_weakness(preamble):
        weaklink = loop_through_numbers(preamble)[1]
        index = 0
        while index < len(numbers):
            found, i1, i2 = check_for_index(index, weaklink)
            if found:
                return get_sum_of_minmax(i1, i2)
            index += 1
        return "Sorry, something went wrong"

    if puzzle == 1:
        return loop_through_numbers(preamble)
    elif puzzle == 2:
        return find_weakness(preamble)


def puzzle_1():
    all_good, value = check_xmas(puzzle=1, preamble=25)
    
    if all_good:
        print(f"""
        Puzzle number 1:
        All numbers in the datastream are working as intended.
        """)
    else:
        print(f"""
        Puzzle number 1:
        We found an irregularity, the first number not matching the rules is {value}
        """)

def puzzle_2():
    total = check_xmas(puzzle=2, preamble=25)
    print(f"""
    Puzzle number 2:
    The total of the min and max is {total}
    """)

puzzle_1()
puzzle_2()