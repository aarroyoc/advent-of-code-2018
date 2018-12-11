import day11

def test_sample():
    assert day11.generate_fuel(122,79,57) == -5
    assert day11.generate_fuel(217,196,39) == 0
    assert day11.generate_fuel(101,153,71) == 4

def test_star_1():
    fuel = day11.generate_table(1133)
    x,y = day11.find_best(fuel)
    assert x == 235
    assert y == 14

def test_star_2():
    fuel = day11.generate_table(1133)
    x,y,size = day11.find_best_any_size(fuel)
    assert x == 237
    assert y == 227
    assert size == 14
