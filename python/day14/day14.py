def day14(inp):
    recipes = list()
    recipes.append(3)
    recipes.append(7)

    a = len(recipes)-2
    b = len(recipes)-1

    while len(recipes) < inp:
        #print("A: %d B: %d" % (a,b))
        #print(recipes)
        recipe = recipes[a]+recipes[b]
        recipe_a = recipe // 10
        recipe_b = recipe % 10
        if recipe_a != 0:
            recipes.append(recipe_a)
        recipes.append(recipe_b)
        a += recipes[a] +1
        b += recipes[b] +1
        a %= len(recipes)
        b %= len(recipes)

    k = len(recipes) - (len(recipes) - inp)

    for i in range(10):
        #print("A: %d B: %d" % (a,b))
        #print(recipes)
        recipe = recipes[a]+recipes[b]
        recipe_a = recipe // 10
        recipe_b = recipe % 10
        if recipe_a != 0:
            recipes.append(recipe_a)
        recipes.append(recipe_b)
        a += recipes[a] +1
        b += recipes[b] +1
        a %= len(recipes)
        b %= len(recipes)
    print(recipes[k:k+10])

def day14_reverse(inp):
    inp = str(inp)
    recipes = str()
    recipes += str(3)
    recipes += str(7)

    a = len(recipes)-2
    b = len(recipes)-1

    while True:
        recipe = int(recipes[a])+int(recipes[b])
        recipe_a = recipe // 10
        recipe_b = recipe % 10
        if recipe_a != 0:
            recipes += str(recipe_a)
        recipes += str(recipe_b)
        a += int(recipes[a]) +1
        b += int(recipes[b]) +1

        a %= len(recipes)
        b %= len(recipes)
        if recipes.find(inp,len(recipes)-10) > -1:
            break
    pos = recipes.find(inp)
    print(pos)

if __name__ == "__main__":
    #day14(846021)
    day14_reverse(846021)