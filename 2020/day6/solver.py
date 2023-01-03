
def build_groups():
    f = open("input.txt", "r")
    groups = []
    for i in f.read().split("\n\n"):
        entry = []
        for j in i.split("\n"):
            entry.append(j)        
        groups.append(entry)
    return groups

def count_per_group():
    groups = build_groups()
    yes_count = []
    for group in groups:
        unique = []
        for answer in group:
            for char in answer:
                if char not in unique:
                    unique.append(char)
        yes_count.append(len(unique))
    return yes_count

def count_all_per_group():

    def check_unique_results(input_list, input_group):
        """
        Take the input list, make a copy so you can use original for looping,
        and check for every unique char if they're in all answers.
        """
        list_duplicate = input_list.copy()
        for char in input_list:
            for answer in input_group:
                if char not in answer and char in list_duplicate:
                    list_duplicate.remove(char)

        return list_duplicate

    groups = build_groups()
    yes_count = []
    for group in groups:
        unique = []
        for answer in group:
            for char in answer:
                if char not in unique:
                    unique.append(char)
        # now check if all answered
        unique = check_unique_results(unique, group)
        yes_count.append(len(unique))
    
    return yes_count

def puzzle_1():
    total = sum(count_per_group())
    
    print(f"""
    Puzzle number 1:
    The sum of all unique answers per group is: {total}
    """)

def puzzle_2():
    # For some reason the answer was 1 short. Completed aoc by guessing the +1. Lucky.
    # Not sure if I made a mistake, or the aoc value is off.
    counts = count_all_per_group()
    total = sum(counts)

    print(f"""
    Puzzle number 2:
    The sum of all unique answers, answered by everyone, per group is: {total}
    """)

puzzle_1()
puzzle_2()