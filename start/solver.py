
def input():
    f = open("input.txt", "r")
    groups = []
    for i in f.read().split("\n\n"):
        entry = []
        for j in i.split("\n"):
            entry.append(j)        
        groups.append(entry)
    return groups



def puzzle_1():
    
    print(f"""
    Puzzle number 1:

    """)

def puzzle_2():

    print(f"""
    Puzzle number 2:

    """)

puzzle_1()
puzzle_2()