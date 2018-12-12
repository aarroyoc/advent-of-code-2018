import re
import sys
from collections import defaultdict

XMIN = -2
XMAX = 0

def find(rules,current):
    if len(current) < 5:
        return ""
    if current in rules:
        return rules[current]
    elif len(current) == 5:
        return "."
    else:
        size = len(current)
        left=find(rules,current[0:size-1])
        right=find(rules,current[size-5:])
        rules[current] = left+right
        return rules[current]

def read_file(file):
    rules = defaultdict(lambda: ".")
    rule_prog = re.compile("([.#]+) => ([.#])")
    with open(file) as f:
        lines = f.readlines()
    state = lines[0].split(": ")[1].strip()
    for line in lines[2:]:
        m = rule_prog.match(line.strip())
        rules[m.group(1)] = m.group(2)
    return state,rules


def print_state(state):
    print(state)

def sum_pots(state):
    n = 0
    for i,c in enumerate(state):
        if c == "#":
            n += i + XMIN
    return n

if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    state,rules = read_file("input.txt")
    XMAX = len(state)+1
    state = "..%s.." % state
    #for _ in range(50000000000):
    sums = list()
    i = 0
    while len(sums) < 3 or sums[-1]-sums[-2] != sums[-2]-sums[-3]:
        state = find(rules,"..%s.." % state)
        if state[0] == "." and state[1] == "." and state[2] == "." and state[3] == ".":
            state = state[2:]
            XMIN += 2
        if state[0] == "#" or state[1] == "#":
            state = "..%s" % state
            XMIN -= 2
        if state[-1] == "#" or state[-2] == "#":
            state = "%s.." % state
            XMAX += 2
        sums.append(sum_pots(state))
        i += 1
    diff = sums[-1]-sums[-2]
    missing = 50000000000 - i
    n = missing*diff + sums[-1]

    print(n)

    
