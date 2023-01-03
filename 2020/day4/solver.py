def build_passports():
    f = open("input.txt", "r")
    passport = []
    for i in f.read().split("\n\n"):
        entry = {}
        for j in i.split():
            k = j.split(":")
            entry[k[0]] = k[1]
        passport.append(entry)
    return passport

def check_passports(req):
    passports = build_passports()
    valid_count = 0
    for i in passports:
        fail = False
        for j in req:
            if j not in i:
                fail = True
        if not fail:
            valid_count += 1
    return valid_count


def passport_rules(passport):
    """
    Checks return true for passed check.
    """

    def check_byr(val):
        return 1920 <= int(val) <= 2002
    
    def check_iyr(val):
        return 2010 <= int(val) <= 2020
    
    def check_eyr(val):
        return 2020 <= int(val) <= 2030
    
    def check_hgt(val):
        splitpoint = len(val) -2
        unit = val[splitpoint:]
        if unit == "cm":
            val = int(val.strip("cm"))
            return 150 <= val <= 193
        elif unit == "in":
            val = int(val.strip("in"))
            return 59 <= val <= 76
        else:
            return False
            

    def check_hcl(val):
        ch1 = val[0] == "#"
        ch2 = len(val) == 7
        allowed = "0123456789abcdef"
        ch3 = True
        for i in val[1:]:
            if i not in allowed:
                ch3 = False
        return ch1 and ch2 and ch3
    
    def check_ecl(val):
        allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ch1 = val in allowed
        ch2 = len(val) == 3
        return ch1 and ch2
    
    def check_pid(val):
        allowed = "0123456789"
        ch1 = len(val) == 9
        ch2 = True
        for i in val:
            if i not in allowed:
                ch2 = False
        return ch1 and ch2
        

    dispatch = {
        "byr": check_byr,
        "iyr": check_iyr,
        "eyr": check_eyr,
        "hgt": check_hgt,
        "hcl": check_hcl,
        "ecl": check_ecl,
        "pid": check_pid,
    }

    required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]

    passing = True
    for i in required:
        if i in passport:
            # print(f"Value {passport[i]} is {dispatch[i](passport[i])}")
            if not dispatch[i](passport[i]):
                passing = False
        else:
            passing = False
    
    return passing

    

def check_passports_extended():
    passports = build_passports()
    valid_count = 0
    for i in passports:
        if passport_rules(i):
            valid_count += 1
    return f"\nPassed passports: {valid_count}"


def puzzle_1():            
    count = check_passports(req=["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"])
    print(count)

def puzzle_2():
    print(check_passports_extended())

puzzle_2()