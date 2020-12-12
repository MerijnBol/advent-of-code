from copy import deepcopy

def input():
    f = open("input.txt", "r")
    return [[x[:1], int(x.strip("\n")[1:])] for x in f.readlines()]

def flip_values(instr):
    """
    Return an instruction with negative values for the opposite actions.
    """
    neg_values = ["S", "W", "L"]
    if instr[0] in neg_values:
        instr[1] = -1 * instr[1]
    return instr

def sail(source_route, starting_point=[0, 0, 90]):
    """
    Sail the ship based on direct movement instructions.
    """
    route = [flip_values(instr) for instr in source_route]
    
    coord = {
        "x": starting_point[0],
        "y": starting_point[1],
        "head": starting_point[2],
    }

    heading_replacement = {
        0: "N",
        90: "E",
        180: "S",
        270: "W"
    }

    for instr in route:
        y_values = ["S", "N"]
        x_values = ["W", "E"]
        headings = ["R", "L"]

        # When to go forward, replace forward command with the correct heading
        if instr[0] == "F":
            instr[0] = heading_replacement[coord["head"]]
            # make sure to pos/neg correct these now too
            instr = flip_values(instr)

        # update the heading for L and R commands:
        if instr[0] in headings:
            new = coord["head"] + instr[1]
            coord["head"] = new % 360

        # Update coordinates
        if instr[0] in y_values:
            coord["y"] += instr[1]
        elif instr[0] in x_values:
            coord["x"] += instr[1]

    return coord


def sail_waypoint(source_route, starting_point=[0, 0, 10, 1]):
    """
    Sail the ship based on a waypoint movement system.
    """
    route = [flip_values(instr) for instr in source_route]
    
    coord = {
        "x": starting_point[0],
        "y": starting_point[1],
    }
    waypoint = {
        "x": starting_point[2],
        "y": starting_point[3],
    }    

    for instr in route:
        y_values = ["S", "N"]
        x_values = ["W", "E"]
        rotations = ["R", "L"]

        # the only actual movement:
        if instr[0] == "F":
            coord["x"] += (instr[1] * waypoint["x"])
            coord["y"] += (instr[1] * waypoint["y"])


        # update the waypoint for L and R commands:
        if instr[0] in rotations:
            x = waypoint["x"]
            y = waypoint["y"]
            rotation = instr[1] % 360
            if rotation == 90:
                waypoint["x"] = y
                waypoint["y"] = -x
            elif rotation == 180:
                waypoint["x"] = -x
                waypoint["y"] = -y
            elif rotation == 270:
                waypoint["x"] = -y
                waypoint["y"] = x

        # Update waypoint coordinates
        if instr[0] in y_values:
            waypoint["y"] += instr[1]
        elif instr[0] in x_values:
            waypoint["x"] += instr[1]

    return coord


def puzzle_1():
    route = deepcopy(input())
    endpoint = sail(route)
    mandist = abs(endpoint["x"]) + abs(endpoint["y"])
    # should be 938

    print(f"""
    Puzzle number 1:
    The endpoint of the first journey is Horizontal: {endpoint["x"]}, vertical: {endpoint["y"]}.
    This gives a Manhattan distance of {mandist}
    """)

def puzzle_2():
    route = deepcopy(input())
    endpoint = sail_waypoint(route)
    mandist = abs(endpoint["x"]) + abs(endpoint["y"])

    print(f"""
    Puzzle number 2:
    The endpoint of the first journey is Horizontal: {endpoint["x"]}, vertical: {endpoint["y"]}.
    This gives a Manhattan distance of {mandist}
    """)

puzzle_1()
puzzle_2()