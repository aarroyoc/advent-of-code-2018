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

with open("input.txt") as f:
    lines = f.readlines()
base,word = find_similar(lines)
final = str()
for i,letter in enumerate(base.strip()):
    if letter == word[i]:
        final += letter
print("FINAL %s"%final)