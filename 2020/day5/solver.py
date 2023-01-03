from math import ceil, floor

def build_seats():
    f = open("input.txt", "r")
    seats = []
    for i in f.readlines():
        # i.replace("F", 0).replace("B", 1).replace("L", 0).replace("R", 1)
        entry = {}
        entry["row"] = i[:7]
        entry["column"] = i[7:10]
        seats.append(entry)
    return seats

def get_seat_id(row, column):
    return row * 8 + column

def decode_binary(string, size):
    range_low = 0
    range_high = size
    for i in string:
        diff = range_high - range_low
        if i == "F" or i == "L":
            range_high = floor(range_high - diff / 2)
        elif i =="B" or i == "R":
            range_low = ceil(range_low + diff / 2)
        else:
            print(f"WRONG SEATNUMBERING: {string}")
            break
    if range_low == range_high:
        return range_low
    else:
        print(f"This string failed: {string}")

def parse_seats():
    seats = build_seats()
    parsed = []
    for i in seats:
        row = decode_binary(i["row"], 127)
        column = decode_binary(i["column"], 7)
        parsed.append((row, column))
    return parsed

def puzzle_1():
    all_ids = []
    for i in parse_seats():
        all_ids.append(get_seat_id(i[0], i[1]))
    
    print(f"""
    Puzzle number 1:
    The heighest seat id is: {max(all_ids)}
    """)

def find_your_seat(seatlist):
    sort = sorted(seatlist)
    for i, item in enumerate(sort):
        # check if next item in list, is + 2 of value.
        if i + 1 < len(sort) and item + 2 == sort[i+1]:
            return item + 1

            
def puzzle_2():
    all_ids = []
    for i in parse_seats():
        all_ids.append(get_seat_id(i[0], i[1]))
    print(f"""
    Puzzle number 2:
    My seat ID = {find_your_seat(all_ids)}
    """)

puzzle_1()
puzzle_2()