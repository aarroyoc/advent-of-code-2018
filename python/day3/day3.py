from dataclasses import dataclass
from collections import defaultdict
import re

@dataclass
class Claim():
    id: int
    x: int
    y: int
    width: int
    height: int

def read_file(file):
    claims = []
    with open(file) as f:
        lines = f.readlines()
    prog = re.compile(r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")
    for line in lines:
        result = prog.match(line.strip())
        claim = Claim(
            id=int(result.group(1)),
            x=int(result.group(2)),
            y=int(result.group(3)),
            width=int(result.group(4)),
            height=int(result.group(5))
        )
        claims.append(claim)
    return claims

def count_overlaps(area):
    overlaps = 0
    for overlap in area.values():
        if overlap > 1:
            overlaps += 1
    return overlaps

def find_nonoverlaping(claims,area):
    for claim in claims:
        overlaps = False
        for i in range(claim.x,claim.x+claim.width):
            for j in range(claim.y,claim.y+claim.height):
                if area[(i,j)] > 1:
                    overlaps = True
        if not overlaps:
            return claim.id 

def day3(file):
    claims = read_file(file)
    area = defaultdict(lambda: 0)
    for claim in claims:
        for i in range(claim.x,claim.x+claim.width):
            for j in range(claim.y,claim.y+claim.height):
                area[(i,j)] += 1
    overlaps = count_overlaps(area)
    non_overlaping = find_nonoverlaping(claims,area)
    return (overlaps,non_overlaping)