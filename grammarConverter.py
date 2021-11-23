RULES = {}

def insert_rule(rule):
    global RULES

    if not rule[0] in RULES:
        # print(rule[0])
        RULES[rule[0]] = []
    RULES[rule[0]].append(rule[1:])

def read_grammar(grammar_file):
    with open(grammar_file) as cfg:
        lines = cfg.readlines()
    grammars = []
    for line in lines:
        line = line.replace("->", "")
        grammars.append(line.split())
    return grammars

def convert_grammar(grammar):
    global RULES
    unitProductions, result = [], []
    index = 0

    for rule in grammar:
        new_rules = []
        # print("This is rule", rule)
        if len(rule) == 2 and rule[1][0] != "'":
            unitProductions.append(rule)
            insert_rule(rule)
            continue
        elif len(rule) > 2:
            terminals = []
            for i, item in enumerate(rule):
                if item[0] == "'" :
                    terminals.append((item,i))
            if terminals:
                # print("This is terminal", terminals)
                for item in terminals:
                    rule[item[1]] = rule[0] + str(index)
                    new_rules += [rule[item[1]], item[0]]
                index += 1
            while len(rule) > 3:
                new_rules += [rule[0] + str(index), rule[1], rule[2]]
                rule = [rule[0]] + [rule[0] + str(index)] + rule[3:]
                index += 1
        insert_rule(rule)
        result.append(rule)
        if new_rules:
            result.append(new_rules)
    while unitProductions:
        rule = unitProductions.pop()
        if rule[1] in RULES:
            for item in RULES[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.append(new_rule)
                else:
                    unitProductions.append(new_rule)
                insert_rule(new_rule)
    return result

