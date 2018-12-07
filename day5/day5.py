import string

def minimize(line,letter):
    line = list(line.strip())
    line = [c for c in line if c.lower() != letter]
    end = False
    while not end:
        end = True
        for i in range(1,len(line)):
            if line[i-1] != line[i] and line[i-1].lower() == line[i].lower():
                end = False
                del line[i-1]
                del line[i-1]
                break
    return len(line)

def react(line):
    new = list()
    for c in line:
        if len(new) > 0 and c != new[-1] and c.lower() == new[-1].lower():
            del new[-1]
        else:
            new += c
    return new

def min_react(line,letter):
    line = [c for c in line if c.lower() != letter]
    return len(react(line))

if __name__ == "__main__":

    with open("input.txt") as f:
        line = f.readline()
    l = react(line)
    """
    line = list(line.strip())
    end = False
    while not end:
        end = True
        for i in range(1,len(line)):
            if line[i-1] != line[i] and line[i-1].lower() == line[i].lower():
                end = False
                del line[i-1]
                del line[i-1]
                break
    """
    print("Units: %d" % (len(l)))
    
    m = min([min_react(line,char) for char in string.ascii_lowercase])
    print("Minimum length: %d" % (m))


