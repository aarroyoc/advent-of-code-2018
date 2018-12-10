from collections import Counter

def changes(base,word):
    changes = 0
    for i,letter in enumerate(base.strip()):
        if not letter == word[i]:
            changes += 1
    return changes

def find_similar(lines):
    for base in lines:
        for word in lines:
            if changes(base,word) == 1:
                return (base,word)

def part2(file):
    with open(file) as f:
        lines = f.readlines()
    base,word = find_similar(lines)
    final = str()
    for i,letter in enumerate(base.strip()):
        if letter == word[i]:
            final += letter
    return final

def part1(file):
    twice = 0
    triple = 0

    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        c = Counter(line)
        if 3 in c.values():
            triple += 1
        if 2 in c.values():
            twice += 1
    total = twice*triple
    return total