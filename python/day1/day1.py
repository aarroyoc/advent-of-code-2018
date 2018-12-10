FREQS = set()

def apply_freq(freq,lines):
    for line in lines:
        signo = line[0:1]
        numero = int(line[1:])
        if signo == "+":
            freq += numero
        elif signo == "-":
            freq -= numero
        if freq in FREQS:
            return (True,freq)
        else:
            FREQS.add(freq)
    return (False,freq)

def part1(file):
    with open(file) as f:
        lines = f.readlines()
    _,freq = apply_freq(0,lines)
    FREQS.clear()
    return freq

def part2(file):
    with open(file) as f:
        lines = f.readlines()
    freq = 0
    while True:
        end,freq = apply_freq(freq,lines)
        if end:
            break
    FREQS.clear()
    return freq