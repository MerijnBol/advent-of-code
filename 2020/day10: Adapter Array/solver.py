
def input():
    listified = [int(x.strip("\n")) for x in open("input.txt", "r").readlines()]
    listified.sort()
    return listified

def adapter_tester(puzzle=1):
    adapts = input()
    # sneak in a 0 at the start of the list, for puzzle 2.
    adapts.insert(0, 0)

    def count_diff():
        diff = ["empty", 0, 0, 0]

        # starting with wall jolts == 0
        previous = 0
        for adapt in adapts:
            delta = adapt - previous
            if 0 < delta < 4:
                diff[delta] += 1
            # prepare next loop
            previous = adapt
        return diff  
    

    def chain_wall_device():
        jumps = count_diff()
        # jolts delta to device is always 3
        jumps[3] += 1
        return jumps[1] * jumps[3]

    # --------------
    # puzzle 2 #
    # --------------

    def find_all_next(list_section, input_index, current, max=3):
        """
        Return all possible next steps based on the list, starting index
        and value of that index.
        """
        # list of tuples
        options = []
        for index, adapt in enumerate(list_section):
            delta = adapt - current
            if delta > 3:
                return options
            if delta > 0:
                options.append((index, adapt))
        # happens when list runs out, and still not over max
        return options
    
    def recursive_solver(list_section):
        """
        For a given section, this function gets all possibilities.
        """
        global ways
        ways = 0
        first_option_list = find_all_next(list_section, 0, list_section[0])

        def recursion(options):
            """
            Keep calling until at the final list index.
            Save that as a solution, and go to next.
            """
            for index, adapt in options:
                if index == (len(list_section) - 1):
                    global ways
                    ways += 1
                    pass
                else:
                    new_options = find_all_next(list_section, index, adapt)
                    recursion(new_options)
        
        # lets go
        recursion(first_option_list)

        # for a list of 1, it also counts as 1 possible step
        if ways == 0:
            return 1
        else:
            return ways

    def split_list():
        """
        Returns sections of the list, broken on max step.
        These sections will always have the same start and end index.
        """
        # start cutting list with first index
        cuts = [0]
        for index, adapt in enumerate(adapts):
            if index + 1 < len(adapts):
                diff = adapts[(index + 1)] - adapt
                if diff == 3:
                    cuts.append(index + 1)
        
        list_sections = []
        for index, cut in enumerate(cuts):
            if cut == cuts[-1]:
                list_sections.append(adapts[cut:])
            else:
                list_sections.append(adapts[cut:(cuts[index + 1])])

        return list_sections
    

    def find_all_possibilities():
        """
        Return all possible combinations
        """
        list_sections = split_list()
        possibilities_steps = []
        for list_section in list_sections:
            possibilities_steps.append(
                recursive_solver(list_section)
            )
        total = 1
        for i in possibilities_steps:
            total = total * i
        return total

    if puzzle == 1:
        return chain_wall_device()
    elif puzzle == 2:
        return find_all_possibilities()

def puzzle_1():
    solution = adapter_tester(puzzle=1)
    print(f"""
    Puzzle number 1:
    The solution is {solution}
    """)

def puzzle_2():
    solution = adapter_tester(puzzle=2)

    print(f"""
    Puzzle number 2:
    the answer is {solution}
    """)

puzzle_1()
puzzle_2()