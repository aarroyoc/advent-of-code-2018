import re
import math

def read_file(file):
    stars = list()
    p = re.compile("position=<([ -][0-9]+), ([ -][0-9]+)> velocity=<([ -][0-9]+), ([ -][0-9]+)>")
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        m = p.match(line.strip())
        try:
            pos_x = int(m.group(1))
        except:
            print(line)
        pos_y = int(m.group(2))
        vel_x = int(m.group(3))
        vel_y = int(m.group(4))
        stars.append([pos_x,pos_y,vel_x,vel_y])
    return stars
def print_stars(stars):
    stars = sorted(stars,key=lambda x: x[0],reverse=True)
    min_width = stars[-1][0]
    max_width = stars[0][0]
    min_height = min(stars,key=lambda x: x[1])[1]
    max_height = max(stars,key=lambda x: x[1])[1]
    s = str()
    for j in range(min_height,max_height+1):
        p = [star for star in stars if star[1] == j]
        # SORT and POP/PUSH
        for i in range(min_width,max_width+1):
            if len(p) == 0:
                s += "."
            else:
                if any(map(lambda star: star[0] == i and star[1] == j,p)):
                    s += "#"
                else:
                    s += "."
        s += "\n"

    return s

def step(stars):
    a = map(lambda x: [x[0]+x[2],x[1]+x[3],x[2],x[3]],stars)
    return list(a)

# LA RESPUESTA CORRECTA TIENE AREA MINIMA
def area(stars):
    stars = sorted(stars,key=lambda x: x[0], reverse=True)
    min_width = stars[-1][0]
    max_width = stars[0][0]
    min_height = min(stars,key=lambda x: x[1])[1]
    max_height = max(stars,key=lambda x: x[1])[1]
    area = (max_width-min_width)*(max_height-min_height)
    return area

def day10(file):
    stars = read_file(file)
    a = area(stars)
    steps = 0
    while area(step(stars)) < a:
        stars = step(stars)
        steps += 1
        a = area(stars)
    return print_stars(stars),steps

if __name__ == "__main__":
    stars = read_file("input.txt")
    a = area(stars)
    steps = 0
    while area(step(stars)) < a:
        stars = step(stars)
        steps += 1
        a = area(stars)
    print(print_stars(stars))
    while True:
        a = input("Continue?(yes/no)")
        if a == "yes":
            stars = step(stars)
            steps += 1 
            print(print_stars(stars))
            print("STEPS: %d" % steps)
        elif a == "no":
            break
