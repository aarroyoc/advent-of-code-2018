from PIL import Image

XMAX = 0
YMAX = 0
STEP = 0

nextDirection = dict()
nextDirection["start"] = "left"
nextDirection["left"] = "center"
nextDirection["center"] = "right"
nextDirection["right"] = "left"

def relative_direction(original,movement):
    print("CROSS")
    if movement == "center":
        return original
    if original == "v":
        if movement == "left":
            return ">"
        else:
            return "<"
    elif original == ">":
        if movement == "left":
            return "^"
        else:
            return "v"
    elif original == "^":
        if movement == "left":
            return "<"
        else:
            return ">"
    else:
        if movement == "left":
            return "v"
        else:
            return "^"

def day13(file):
    global XMAX
    global YMAX
    global STEP
    plano = dict()
    carts = list()
    with open(file) as f:
        lines = f.readlines()
    YMAX = len(lines)
    XMAX = len(lines[0])
    for y,line in enumerate(lines):
        for x,char in enumerate(line):
            # SI HAY UN CARRITO, DEDUCIR TIPO DE VIA
            if char == "^" or char == "v" or char == "<" or char == ">":
                if (x,y-1) in plano:
                    plano[(x,y)] = "|"
                else:
                    plano[(x,y)] = "-"
                carts.append([x,y,char,"left"])
            else:
                plano[(x,y)] = char
    
    end = False
    while not end:
        carts.sort(key=lambda x: x[1])
        carts.sort(key=lambda x: x[0])

        for cart in carts:
            # CHECK CRASH
            for crt in carts:
                if cart[0] == crt[0] and cart[1] == crt[1] and id(cart) != id(crt):
                    print("CRASH AT %d-%d" % (cart[0],cart[1]))
                    end = True
            try:
                x = cart[0]
                y = cart[1]
                print(cart)
                if cart[2] == ">":
                    if plano[(x+1,y)] == "/":
                        cart[2] = "^"
                    elif plano[(x+1,y)] == "\\":
                        cart[2] = "v"
                    elif plano[(x+1,y)] == "+":
                        cart[2] = relative_direction(cart[2],cart[3])
                        cart[3] = nextDirection[cart[3]]
                    cart[0] += 1
                elif cart[2] == "<":
                    if plano[(x-1,y)] == "/":
                        cart[2] = "v"
                    elif plano[(x-1,y)] == "\\":
                        cart[2] = "^"
                    elif plano[(x-1,y)] == "+":
                        cart[2] = relative_direction(cart[2],cart[3])
                        cart[3] = nextDirection[cart[3]]
                    cart[0] -= 1
                elif cart[2] == "^":
                    if plano[(x,y-1)] == "/":
                        cart[2] = ">"
                    elif plano[(x,y-1)] == "\\":
                        cart[2] = "<"
                    elif plano[(x,y-1)] == "+":
                        cart[2] = relative_direction(cart[2],cart[3])
                        cart[3] = nextDirection[cart[3]]
                    cart[1] -= 1
                elif cart[2] == "v":
                    print()
                    if plano[(x,y+1)] == "/":
                        cart[2] = "<"
                    elif plano[(x,y+1)] == "\\":
                        cart[2] = ">"
                    elif plano[(x,y+1)] == "+":
                        cart[2] = relative_direction(cart[2],cart[3])
                        cart[3] = nextDirection[cart[3]]
                    cart[1] += 1
            except:
                breakpoint()
        STEP += 1
        print_train(plano,carts)

def print_train(plano,carts):
    im = Image.new("RGB",(XMAX,YMAX))
    for x,y in plano:
        if plano[(x,y)] != " ":
            im.putpixel((x,y),(255,255,255))
        if plano[(x,y)] == "+":
            im.putpixel((x,y),(120,120,120))
    for cart in carts:
        if cart[2] == ">":
            im.putpixel((cart[0],cart[1]),(255,0,0))
        elif cart[2] == "<":
            im.putpixel((cart[0],cart[1]),(0,255,0))
        elif cart[2] == "^":
            im.putpixel((cart[0],cart[1]),(0,0,255))
        else:
            im.putpixel((cart[0],cart[1]),(0,120,120))

    im.save("train-%d.png" % STEP,"PNG")

if __name__ == "__main__":
    day13("input_net.txt")