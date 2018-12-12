import day12
import day12_2

def test_sample():
    assert day12.day12("day12/prueba.txt") == 325

def test_star_1():
    assert day12.day12("day12/input.txt") == 4110

def test_star_2():
    assert day12_2.day12("day12/input.txt") == 2650000000466