import re
from collections import defaultdict

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

def parse_state(pots):
    state = dict()
    for i,p in enumerate(pots):
        state[i] = p
    return state

def find(rules,current):
    if current in rules:
        return rules[current]
    else:
        size = len(current)
        mid = size // 2
        left = find(rules,current[0:mid])
        right = find(rules,current[mid:])
        rules[current] = left + right
        return rules[current]


def hash_iter(state,rules):
    xmin = min(state.keys())
    xmax = max(state.keys())
    par_states = (len(state) // 10) * 10
    current = ["%c" % state[x] for x in range(xmin,xmin+par_states)]
    missing = ["%c" % state[x] for x in range(xmin+par_states,xmax)]
    missing = len(state) % 10


def iter(state,rules):
    new_state = dict()
    xmin = min(state.keys())
    xmax = max(state.keys())
    for x in range(xmin-2,xmax+3):
        current = ("%c%c%c%c%c" % (
                    state.get(x-2,"."),
                    state.get(x-1,"."),
                    state.get(x,"."),
                    state.get(x+1,"."),
                    state.get(x+2,".")
                    ))
        new = rules[current]
        if new == "#" or xmin <= x <= xmax:
            new_state[x] = new
    return new_state

def sum_pots(state):
    n = 0
    for pot in state:
        if state[pot] == "#":
            n += pot
    return n

def print_state(state):
    xmin = min(state.keys())
    xmax = max(state.keys())
    s = str("XMIN %d : " % xmin)
    for x in range(xmin-2,xmax+3):
        s += state.get(x,".")
    print(s)


def day12(file):
    state,rules = read_file(file)
    state = parse_state(state)
    for i in range(3000):
        #print_state(state)
        state = iter(state,rules)
    #print_state(state)
    n = sum_pots(state)
    print(n)

if __name__ == "__main__":
    day12("input.txt")