from collections import Counter

twice = 0
triple = 0

with open("input.txt") as f:
    lines = f.readlines()
for line in lines:
    c = Counter(line)
    if 3 in c.values():
        triple += 1
    if 2 in c.values():
        twice += 1
total = twice*triple
print("CHECKSUM: %d" % total)