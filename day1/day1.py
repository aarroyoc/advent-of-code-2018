FREQS = set()

def apply_freq(freq):
    with open("input.txt") as f:
        lines = f.readlines()
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

if __name__ == "__main__":
    freq = 0
    while True:
        end,freq = apply_freq(freq)
        if end:
            break
    print("FREQ FINAL: %d" % freq)