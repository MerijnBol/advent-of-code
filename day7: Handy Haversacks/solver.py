
def build_rules():
    f = open("input.txt", "r")
    rules = []
    for i in f.read().split("\n"):
        entry = {}
        entry["parent"] = i.split("bags")[0].strip()
        entry["childs"] = []
        if "contain" in i:
            for rule in i.split("contain")[1].strip().split(", "):
                if "no other" in rule:
                    break
                single = {}
                single["count"] = rule[0]
                single["color"] = rule[1:].strip("bags.").strip()
                entry["childs"].append(single)
            rules.append(entry)
    return rules

rules = build_rules()

def get_containers(target="shiny gold"):
    
    def get_parents(rules, target):
        containers = []
        for rule in rules:
            can_contain = False
            for child in rule["childs"]:
                if child["color"] == target:
                    can_contain = True
            if can_contain:
                containers.append(rule["parent"])
        return containers
    

    total_containers = []
    containers = get_parents(rules, target)
    total_containers = total_containers + containers
    while len(containers) != 0:
        looplist = containers.copy()
        containers = []
        for color in looplist:
            containers = containers + get_parents(rules, color)
        for color in containers:
            if color not in total_containers:
                total_containers.append(color)
    return(total_containers)

def get_total_content(target="shiny gold"):
    
    
    def get_childs(target=target):
        childs = []
        for rule in rules:
            if rule["parent"] == target:
                for child in rule["childs"]:
                    childs += int(child["count"]) * [child["color"]]
            # for child in rule["childs"]:
            #     if child["color"] == target:
            #         can_contain = True
            # if can_contain:
            #     childs.append(rule["parent"])
        return childs
    
    total_childs = []
    childs = get_childs(target)
    total_childs = total_childs + childs
    while True:
        looplist = childs.copy()
        childs = []
        for color in looplist:
            childs = childs + get_childs(color)
        total_childs += childs
        if childs == []:
            # no more children found
            break
    return(total_childs)
    

def puzzle_1():
    target = "shiny gold"
    list_of_containers = get_containers(target)
    count = len(list_of_containers)
    
    print(f"""
    Puzzle number 1:
    The amount of bags which can, somewhere, have a '{target}' bag in them, is {count}. 
    """)

def puzzle_2():
    target = "shiny gold"
    childs = get_total_content(target)
    count = len(childs)
    print(f"""
    Puzzle number 2:
    The amount of bags which will go inside the '{target}' bag is {count}.
    """)

puzzle_1()
puzzle_2()