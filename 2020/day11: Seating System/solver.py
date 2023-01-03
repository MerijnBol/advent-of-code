from copy import deepcopy

def input():
    """
    floor (.)
    empty seat (L)
    occupied seat (#)
    """
    f = open("input.txt", "r")
    return [[j for j in x.strip("\n")] for x in f.readlines()]

def get_markers_insight(seats):
    """
    Return a dict which for each seat contains coordinates of closest seats.
    """

    last_row = len(seats) - 1
    # assuming all rows are equal length
    last_seat = len(seats[0]) - 1

    def left(row, seat):
        seat -= 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if seat > 0:
                seat -= 1
            else:
                return False
        return (row, seat)

    def right(row, seat):
        seat += 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if seat < last_seat:
                seat += 1
            else:
                return False
        return (row, seat)

    def top(row, seat):
        row -= 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if row > 0:
                row -= 1
            else:
                return False
        return (row, seat)
        

    def bottom(row, seat):
        row += 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if row < last_row:
                row += 1
            else:
                return False
        return (row, seat)

    def topleft(row, seat):
        row -= 1
        seat -= 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if row > 0 and seat > 0:
                row -= 1
                seat -= 1
            else:
                return False
        return (row, seat)

    def topright(row, seat):
        row -= 1
        seat += 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if row > 0 and seat < last_seat:
                row -= 1
                seat += 1
            else:
                return False
        return (row, seat)

    def bottomleft(row, seat):
        row += 1
        seat -= 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if seat > 0 and row < last_row:
                row += 1
                seat -= 1
            else:
                return False
        return (row, seat)

    def bottomright(row, seat):
        row += 1
        seat += 1
        if seat < 0 or row < 0:
            return False
        while seats[row][seat] != "L":
            if row < last_row and seat < last_seat:
                row += 1
                seat += 1
            else:
                return False
        return (row, seat)
    
    worklist = [left, right, top, bottom, topleft, topright, bottomleft, bottomright]

    markers = {}
    # floop over all row numbers
    for row in range(len(seats)):
        # loop over all seat numbers
        for seat in range(len(seats[row])):
            # list of markers, with seat coordinate as key
            markers[(row, seat)] = []
            # do all closest seat checks
            for work in worklist:
                try:
                    if work(row, seat) is not False:
                        markers[(row, seat)].append( work(row, seat) )
                except:
                    IndexError
    return markers

def update_seating(seats, markers, threshhold=4):

    def adjacent_occupancy(coord, markers=markers):
        occupied = 0
        for row, seat in markers[coord]:
            if seats[row][seat] == "#":
                occupied += 1
        return occupied

    new_seats = deepcopy(seats)
    # floop over all row numbers
    for row in range(len(seats)):
        # loop over all seat numbers
        for seat in range(len(seats[row])):
            neighbours = adjacent_occupancy((row, seat))
            if seats[row][seat] == "L" and neighbours == 0:
                new_seats[row][seat] = "#"
            elif seats[row][seat] == "#" and neighbours >= (threshhold):
                new_seats[row][seat] = "L"

    return new_seats


def count_occupied(seats):
    occupied = 0
    # floop over all row numbers
    for row in range(len(seats)):
        # loop over all seat numbers
        for seat in range(len(seats[row])):
            if seats[row][seat] == "#":
                occupied += 1
    return occupied


def get_markers(seats):
    """
    Return a dict which for each seat contains coordinates of closest seats.
    """

    last_row = len(seats) - 1
    # assuming all rows are equal length
    last_seat = len(seats[0]) - 1

    def left(row, seat):
        if seat > 0:
            return (row, seat - 1)

    def right(row, seat):
        if seat < last_seat:
            return (row, seat + 1)

    def top(row, seat):
        if row > 0:
            return (row - 1, seat)

    def bottom(row, seat):
        if row < last_row:
            return (row + 1, seat)

    def topleft(row, seat):
        if row > 0 and seat > 0:
            return (row - 1, seat - 1)

    def topright(row, seat):
        if row > 0 and seat < last_seat:
            return (row - 1, seat + 1)

    def bottomleft(row, seat):
        if seat > 0 and row < last_row:
            return (row + 1, seat - 1)

    def bottomright(row, seat):
        if row < last_row and seat < last_seat:
            return (row + 1, seat + 1)
    
    worklist = [left, right, top, bottom, topleft, topright, bottomleft, bottomright]

    markers = {}
    # floop over all row numbers
    for row in range(len(seats)):
        # loop over all seat numbers
        for seat in range(len(seats[row])):
            # list of markers, with seat coordinate as key
            markers[(row, seat)] = []
            # do all closest seat checks
            for work in worklist:
                try:
                    if work(row, seat) is not None:
                        markers[(row, seat)].append( work(row, seat) )
                except:
                    IndexError
    return markers

def puzzle_1():
    seats = deepcopy(input())
    markers = get_markers(seats)

    old_seats = []
    while old_seats != seats:
        old_seats = deepcopy(seats)
        seats = deepcopy(update_seating(seats, markers))
    
    occupants = count_occupied(old_seats)

    print(f"""
    Puzzle number 1:
    The total number of taken seats is {occupants}
    """)

def puzzle_2():
    seats = deepcopy(input())
    markers = get_markers_insight(seats)

    old_seats = []
    while old_seats != seats:
        old_seats = deepcopy(seats)
        seats = deepcopy(update_seating(seats, markers, 5))
    
    occupants = count_occupied(old_seats)

    print(f"""
    Puzzle number 2:
    The total number of taken seats is {occupants}
    """)

puzzle_1()
puzzle_2()