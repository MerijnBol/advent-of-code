
def get_floor():
    f = open("input.txt", "r")
    floor = 0
    for num, i in enumerate(f.read()):
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        if floor == -1:
            return num + 1
    return floor


def puzzle_1():
    
    print(f"""
    Puzzle number 1:
    THe resulting floor is {get_floor()}
    """)

def puzzle_2():

    print(f"""
    Puzzle number 2:

    """)

puzzle_1()
puzzle_2()