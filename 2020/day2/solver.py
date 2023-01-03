import math

def parse_input(input):
    passwords = []
    for line in input:
        params = {}
        dirty=line.split()
        minmax=[int(i) for i in dirty[0].split('-')]
        params["min"] = min(minmax)
        params["max"] = max(minmax)
        params["check"] = dirty[1].rstrip(":")
        params["psswd"] = dirty[2]
        passwords.append(params)
    return passwords

def check_passwords(passwords: list):
    amount_of_passwords = 0
    for line in passwords:
        char_count = line["psswd"].count(line["check"])
        if char_count >= line["min"] and char_count <= line["max"]:
            amount_of_passwords += 1
    return amount_of_passwords

def puzzle1():
    passwords = parse_input(open("input.txt", "r"))
    amount = check_passwords(passwords)
    print(amount)

def check_policy_nr2(passwords: list):

    def check_in_string(string, index, check):
        index -= 1
        try:
            if string[index] == check:
                return True
            else:
                return False
        except IndexError:
            return False

    def check_policy_logic(line):
        occ1 = check_in_string(line["psswd"], line["min"], line["check"])
        occ2 = check_in_string(line["psswd"], line["max"], line["check"])
        if occ2 and not occ1 or occ1 and not occ2:
            return True

    amount_of_passwords = 0
    for line in passwords:
        if check_policy_logic(line):
            amount_of_passwords += 1
    return amount_of_passwords

def puzzle2():
    passwords = parse_input(open("input.txt", "r"))
    amount = check_policy_nr2(passwords)
    print(amount)

puzzle2()
