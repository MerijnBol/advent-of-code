
def build_rules():
    return [[x.split()[0], x.split()[1]] for x in open("input.txt", "r").readlines() if x != ""]

def interpreter(rules):
    
    newline = 0
    accumulator = 0
    while newline < len(rules):
        
        jumped = False
        line = newline

        # dispatch[rules[line][0]](rules[line][1])
        if rules[line][0] == "acc":
            accumulator += int(rules[line][1])
        elif rules[line][0] == "jmp":
            newline += int(rules[line][1])
            jumped = True
        elif rules[line][0] == "nop":
            pass

        if not jumped:
            newline += 1

        # check for infintie loop
        if rules[line] == "overwritten":
            return accumulator
        else:
            rules[line] = "overwritten"
       


def interpreter_2():
    
    base_rules = build_rules()
    
    def test_change(tried):
        newline = 0
        accumulator = 0
        used_lines = []
        rulechange = False
        tried_line = 0

        while newline < len(base_rules):
            rules = build_rules()
            jumped = False
            line = newline

            # check for infinite loop
            if line in used_lines:
                return False, tried_line, accumulator
            
            used_lines.append(line)

            # try changing rules, once per game loop
            if not rulechange and line not in tried and rules[line][0] == "jmp":
                rules[line][0] = "nop"
                rulechange = True
                tried_line = line
            elif not rulechange and line not in tried and rules[line][0] == "nop":
                rules[line][0] = "jmp"
                rulechange = True
                tried_line = line
            
            # the interpreter
            if rules[line][0] == "acc":
                accumulator += int(rules[line][1])
            elif rules[line][0] == "jmp":
                newline += int(rules[line][1])
                jumped = True
            elif rules[line][0] == "nop":
                pass

            # go to new command line
            if not jumped:
                newline += 1
            
            # check for completed program
            # print(f"new line is {line}, rules length is {len(rules)}")
            if newline == len(rules):
                return True, line, accumulator

    # loop over all possible changes until something works
    tried = []
    while len(tried) < len(base_rules):
        completed, line, accumulator = test_change(tried)
        if completed:
            return accumulator
        else:
            tried.append(line)

    


print("the answer is: ", interpreter_2())

