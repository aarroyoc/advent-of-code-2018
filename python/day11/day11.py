from collections import defaultdict

def generate_fuel(x,y,idg):
    fuel = (((x+10)*y)+idg)*(x+10)
    fuel %= 1000
    fuel = (fuel // 100) - 5
    return fuel

def generate_table(idg):
    fuel = {(x,y,size):0 for x in range(1,301) for y in range(1,301) for size in range(1,301)} 
    for x in range(1,301):
        for y in range(1,301):
            fuel[(x,y,1)] = generate_fuel(x,y,idg)
    return fuel

def find_best(fuel):
    max_point = [-1,-1]
    max_score = -1
    for x in range(1,301):
        for y in range(1,301):
            if x+3 > 301 or y+3 > 301:
                continue
            score = fuel[(x,y,1)]+fuel[(x+1,y,1)]+fuel[(x+2,y,1)]+fuel[(x,y+1,1)]+fuel[(x+1,y+1,1)]+fuel[(x+2,y+1,1)]+fuel[(x,y+2,1)]+fuel[(x+1,y+2,1)]+fuel[(x+2,y+2,1)]
            if score > max_score:
                max_score = score
                max_point = [x,y]
    return max_point[0],max_point[1]

def find_best_any_size(fuel):
    max_score = -1
    max_point = [-1,-1,-1]
    for size in range(2,300+1):
        for x in range(1,301):
            for y in range(1,301):
                if x+size > 301 or y+size > 301:
                    continue
                if size % 2 == 0:
                    mid = size // 2
                    fuel[(x,y,size)] = fuel[(x+mid,y,mid)]+fuel[(x,y+mid,mid)]+fuel[(x+mid,y+mid,mid)]+fuel[(x,y,mid)]
                else:
                    fuel[(x,y,size)] = fuel[(x,y,size-1)]
                    for i in range(x,x+size-1):
                        fuel[(x,y,size)] += fuel[(i,y+size-1,1)]
                    for j in range(y,y+size-1):
                        fuel[(x,y,size)] += fuel[(x+size-1,j,1)]
                    fuel[(x,y,size)] += fuel[(x+size-1,y+size-1,1)]
                score = fuel[(x,y,size)]
                if score > max_score:
                    max_score = score
                    max_point = [x,y,size]
    return max_point[0],max_point[1],max_point[2]


def day11():
    fuel = generate_table(1133)
    x,y = find_best(fuel)
    print("BEST POINT: %d,%d" % (x,y))
    x,y,size = find_best_any_size(fuel)
    print("BEST POINT ANY SIZE: %d,%d,%d" % (x,y,size))

if __name__ == "__main__":
    day11()
